import { getStore } from "@netlify/blobs";
import { createHmac, randomBytes, timingSafeEqual } from "node:crypto";

const AUTH_STORE = "gsc-auth";
const CACHE_STORE = "gsc-cache";
const OAUTH_SCOPES = [
  "openid",
  "email",
  "https://www.googleapis.com/auth/webmasters.readonly",
  "https://www.googleapis.com/auth/drive.file"
].join(" ");
const DEFAULT_REDIRECT = "https://robert-morong-research.netlify.app/gsc/callback";
const ALLOWED_EMAIL = process.env.GSC_ALLOWED_EMAIL || "morongrobert@gmail.com";

export function getConfig() {
  return {
    clientId: process.env.GSC_GOOGLE_CLIENT_ID || "",
    clientSecret: process.env.GSC_GOOGLE_CLIENT_SECRET || "",
    redirectUri: process.env.GSC_REDIRECT_URI || DEFAULT_REDIRECT,
    stateSecret: process.env.GSC_OAUTH_STATE_SECRET || "",
    allowedEmail: ALLOWED_EMAIL,
  };
}

export function json(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      ...headers,
    },
  });
}

export function html(markup, status = 200, headers = {}) {
  return new Response(markup, {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "no-store",
      ...headers,
    },
  });
}

function b64url(input) {
  return Buffer.from(input).toString("base64url");
}

function sign(value, secret) {
  return createHmac("sha256", secret).update(value).digest("base64url");
}

export function makeState() {
  const { stateSecret } = getConfig();
  if (!stateSecret) throw new Error("GSC_OAUTH_STATE_SECRET is not configured");
  const payload = b64url(JSON.stringify({
    ts: Date.now(),
    nonce: randomBytes(18).toString("base64url"),
  }));
  return payload + "." + sign(payload, stateSecret);
}

export function verifyState(state) {
  const { stateSecret } = getConfig();
  if (!stateSecret || !state || !state.includes(".")) return false;
  const [payload, sig] = state.split(".");
  const expected = sign(payload, stateSecret);
  const a = Buffer.from(sig);
  const b = Buffer.from(expected);
  if (a.length !== b.length || !timingSafeEqual(a, b)) return false;
  try {
    const parsed = JSON.parse(Buffer.from(payload, "base64url").toString("utf8"));
    return Number.isFinite(parsed.ts) && Date.now() - parsed.ts < 10 * 60 * 1000;
  } catch {
    return false;
  }
}

export function makeSessionCookie(email) {
  const { stateSecret } = getConfig();
  const payload = b64url(JSON.stringify({ email, ts: Date.now() }));
  const sig = sign(payload, stateSecret);
  return "gsc_session=" + payload + "." + sig + "; Path=/gsc; HttpOnly; Secure; SameSite=Lax; Max-Age=2592000";
}

export function hasValidSession(req) {
  const cookie = req.headers.get("cookie") || "";
  const match = cookie.match(/(?:^|;\s*)gsc_session=([^;]+)/);
  if (!match) return false;
  const { stateSecret, allowedEmail } = getConfig();
  const [payload, sig] = match[1].split(".");
  if (!payload || !sig || !stateSecret) return false;
  const expected = sign(payload, stateSecret);
  const a = Buffer.from(sig);
  const b = Buffer.from(expected);
  if (a.length !== b.length || !timingSafeEqual(a, b)) return false;
  try {
    const data = JSON.parse(Buffer.from(payload, "base64url").toString("utf8"));
    return data.email === allowedEmail && Date.now() - data.ts < 30 * 24 * 60 * 60 * 1000;
  } catch {
    return false;
  }
}

export function oauthUrl() {
  const { clientId, redirectUri } = getConfig();
  if (!clientId) throw new Error("GSC_GOOGLE_CLIENT_ID is not configured");
  const qs = new URLSearchParams({
    client_id: clientId,
    redirect_uri: redirectUri,
    response_type: "code",
    scope: OAUTH_SCOPES,
    access_type: "offline",
    prompt: "consent",
    include_granted_scopes: "true",
    state: makeState(),
  });
  return "https://accounts.google.com/o/oauth2/v2/auth?" + qs.toString();
}

export async function exchangeCode(code) {
  const { clientId, clientSecret, redirectUri } = getConfig();
  if (!clientId || !clientSecret) throw new Error("Google OAuth client credentials are not configured");
  const body = new URLSearchParams({
    code,
    client_id: clientId,
    client_secret: clientSecret,
    redirect_uri: redirectUri,
    grant_type: "authorization_code",
  });
  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body,
  });
  const data = await res.json();
  if (!res.ok) throw new Error("OAuth token exchange failed: " + JSON.stringify(data));
  return data;
}

async function authStore() {
  return getStore(AUTH_STORE);
}
async function cacheStore() {
  return getStore(CACHE_STORE);
}

export async function getSavedAuth() {
  const store = await authStore();
  return await store.get("google-oauth", { type: "json", consistency: "strong" });
}

export async function saveAuth(tokens, email) {
  const store = await authStore();
  const previous = await store.get("google-oauth", { type: "json", consistency: "strong" });
  const merged = {
    ...(previous || {}),
    ...tokens,
    refresh_token: tokens.refresh_token || previous?.refresh_token || "",
    email,
    saved_at: new Date().toISOString(),
  };
  await store.setJSON("google-oauth", merged);
  return merged;
}

async function refreshAccessToken(refreshToken) {
  const { clientId, clientSecret } = getConfig();
  const body = new URLSearchParams({
    client_id: clientId,
    client_secret: clientSecret,
    refresh_token: refreshToken,
    grant_type: "refresh_token",
  });
  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body,
  });
  const data = await res.json();
  if (!res.ok) throw new Error("Google token refresh failed: " + JSON.stringify(data));
  return data.access_token;
}

export async function accessToken() {
  const auth = await getSavedAuth();
  if (!auth?.refresh_token) throw new Error("Google OAuth has not been completed yet");
  return await refreshAccessToken(auth.refresh_token);
}

export async function fetchGoogle(path, options = {}) {
  const token = await accessToken();
  const headers = new Headers(options.headers || {});
  headers.set("authorization", "Bearer " + token);
  if (options.body && !headers.has("content-type")) headers.set("content-type", "application/json");
  const res = await fetch(path, { ...options, headers });
  const text = await res.text();
  const data = text ? JSON.parse(text) : null;
  if (!res.ok) throw new Error("Google API " + res.status + ": " + JSON.stringify(data));
  return data;
}

export async function fetchUserEmail(accessTokenValue) {
  const res = await fetch("https://openidconnect.googleapis.com/v1/userinfo", {
    headers: { authorization: "Bearer " + accessTokenValue },
  });
  const data = await res.json();
  if (!res.ok) throw new Error("Unable to verify Google account email");
  return data.email || "";
}

function isoDate(d) {
  return d.toISOString().slice(0, 10);
}
function shift(date, days) {
  const d = new Date(date);
  d.setUTCDate(d.getUTCDate() + days);
  return d;
}
export function settledRanges() {
  const now = new Date();
  const end = shift(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()), -3);
  const start = shift(end, -27);
  const previousEnd = shift(start, -1);
  const previousStart = shift(previousEnd, -27);
  return {
    current: { startDate: isoDate(start), endDate: isoDate(end) },
    previous: { startDate: isoDate(previousStart), endDate: isoDate(previousEnd) },
  };
}

async function searchAnalytics(siteUrl, body) {
  return await fetchGoogle(
    "https://searchconsole.googleapis.com/webmasters/v3/sites/" +
      encodeURIComponent(siteUrl) +
      "/searchAnalytics/query",
    { method: "POST", body: JSON.stringify(body) }
  );
}

function normalizeTotals(data) {
  const row = data?.rows?.[0] || {};
  return {
    clicks: row.clicks || 0,
    impressions: row.impressions || 0,
    ctr: row.ctr || 0,
    position: row.position || 0,
  };
}

function normalizeRows(data, dimension) {
  return (data?.rows || []).map((row) => ({
    [dimension]: row.keys?.[0] || "",
    clicks: row.clicks || 0,
    impressions: row.impressions || 0,
    ctr: row.ctr || 0,
    position: row.position || 0,
  }));
}

export async function buildPortfolio() {
  const ranges = settledRanges();
  const sitesData = await fetchGoogle("https://www.googleapis.com/webmasters/v3/sites");
  const siteEntries = sitesData?.siteEntry || [];
  const sites = [];

  for (const site of siteEntries) {
    const siteUrl = site.siteUrl;
    const result = {
      siteUrl,
      permissionLevel: site.permissionLevel || null,
      current: null,
      previous: null,
      delta: null,
      queries: [],
      pages: [],
      sitemaps: [],
      errors: [],
    };

    try {
      const [current, previous, queries, pages, sitemaps] = await Promise.all([
        searchAnalytics(siteUrl, { ...ranges.current, type: "web", rowLimit: 1 }),
        searchAnalytics(siteUrl, { ...ranges.previous, type: "web", rowLimit: 1 }),
        searchAnalytics(siteUrl, { ...ranges.current, type: "web", dimensions: ["query"], rowLimit: 50 }),
        searchAnalytics(siteUrl, { ...ranges.current, type: "web", dimensions: ["page"], rowLimit: 100 }),
        fetchGoogle("https://www.googleapis.com/webmasters/v3/sites/" + encodeURIComponent(siteUrl) + "/sitemaps"),
      ]);
      result.current = normalizeTotals(current);
      result.previous = normalizeTotals(previous);
      result.delta = {
        clicks: result.current.clicks - result.previous.clicks,
        impressions: result.current.impressions - result.previous.impressions,
      };
      result.queries = normalizeRows(queries, "query");
      result.pages = normalizeRows(pages, "page");
      result.sitemaps = (sitemaps?.sitemap || []).map((s) => ({
        path: s.path,
        lastSubmitted: s.lastSubmitted || null,
        lastDownloaded: s.lastDownloaded || null,
        isPending: !!s.isPending,
        warnings: Number(s.warnings || 0),
        errors: Number(s.errors || 0),
        contents: s.contents || [],
      }));
    } catch (error) {
      result.errors.push(String(error?.message || error));
    }
    sites.push(result);
  }

  const totals = sites.reduce(
    (acc, s) => {
      acc.clicks += s.current?.clicks || 0;
      acc.impressions += s.current?.impressions || 0;
      acc.previousClicks += s.previous?.clicks || 0;
      acc.previousImpressions += s.previous?.impressions || 0;
      return acc;
    },
    { clicks: 0, impressions: 0, previousClicks: 0, previousImpressions: 0 }
  );

  const portfolio = {
    generatedAt: new Date().toISOString(),
    source: "Google Search Console API",
    ranges,
    totals: {
      ...totals,
      deltaClicks: totals.clicks - totals.previousClicks,
      deltaImpressions: totals.impressions - totals.previousImpressions,
    },
    siteCount: sites.length,
    sites,
  };

  const store = await cacheStore();
  await store.setJSON("portfolio-latest", portfolio);
  return portfolio;
}

export async function latestPortfolio() {
  const store = await cacheStore();
  return await store.get("portfolio-latest", { type: "json", consistency: "strong" });
}

function fmtPct(x) {
  return ((x || 0) * 100).toFixed(2) + "%";
}

export function portfolioMarkdown(p) {
  const lines = [];
  lines.push("# Google Search Console Portfolio Snapshot");
  lines.push("");
  lines.push("Generated: " + p.generatedAt);
  lines.push("Source: Google Search Console API");
  lines.push("Current range: " + p.ranges.current.startDate + " to " + p.ranges.current.endDate);
  lines.push("Previous range: " + p.ranges.previous.startDate + " to " + p.ranges.previous.endDate);
  lines.push("");
  lines.push("## Portfolio totals");
  lines.push("");
  lines.push("- Clicks: " + p.totals.clicks + " (" + (p.totals.deltaClicks >= 0 ? "+" : "") + p.totals.deltaClicks + ")");
  lines.push("- Impressions: " + p.totals.impressions + " (" + (p.totals.deltaImpressions >= 0 ? "+" : "") + p.totals.deltaImpressions + ")");
  lines.push("");
  for (const site of p.sites) {
    lines.push("## " + site.siteUrl);
    lines.push("");
    lines.push("- Permission: " + (site.permissionLevel || "unknown"));
    if (site.current) {
      lines.push("- Current: " + site.current.clicks + " clicks, " + site.current.impressions + " impressions, CTR " + fmtPct(site.current.ctr) + ", avg position " + site.current.position.toFixed(2));
      lines.push("- Change: " + (site.delta.clicks >= 0 ? "+" : "") + site.delta.clicks + " clicks, " + (site.delta.impressions >= 0 ? "+" : "") + site.delta.impressions + " impressions");
    }
    if (site.errors?.length) lines.push("- Errors: " + site.errors.join(" | "));
    lines.push("");
    lines.push("### Top queries");
    lines.push("");
    for (const q of site.queries.slice(0, 25)) {
      lines.push("- " + q.query + ": " + q.clicks + " clicks, " + q.impressions + " impressions, pos " + q.position.toFixed(2) + ", CTR " + fmtPct(q.ctr));
    }
    lines.push("");
    lines.push("### Top pages");
    lines.push("");
    for (const page of site.pages.slice(0, 25)) {
      lines.push("- " + page.page + ": " + page.clicks + " clicks, " + page.impressions + " impressions, pos " + page.position.toFixed(2) + ", CTR " + fmtPct(page.ctr));
    }
    lines.push("");
    lines.push("### Sitemaps");
    lines.push("");
    if (!site.sitemaps.length) lines.push("- None returned");
    for (const s of site.sitemaps) {
      lines.push("- " + s.path + " | submitted " + (s.lastSubmitted || "unknown") + " | downloaded " + (s.lastDownloaded || "unknown") + " | warnings " + s.warnings + " | errors " + s.errors);
    }
    lines.push("");
  }
  return lines.join("\n");
}

async function driveStateStore() {
  return getStore("gsc-drive");
}

async function uploadNewDriveFile(name, mimeType, content) {
  const token = await accessToken();
  const boundary = "gsc_" + randomBytes(12).toString("hex");
  const body =
    "--" + boundary + "\r\n" +
    "Content-Type: application/json; charset=UTF-8\r\n\r\n" +
    JSON.stringify({ name, mimeType }) + "\r\n" +
    "--" + boundary + "\r\n" +
    "Content-Type: " + mimeType + "\r\n\r\n" +
    content + "\r\n" +
    "--" + boundary + "--";
  const res = await fetch("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,webViewLink", {
    method: "POST",
    headers: {
      authorization: "Bearer " + token,
      "content-type": "multipart/related; boundary=" + boundary,
    },
    body,
  });
  const data = await res.json();
  if (!res.ok) throw new Error("Drive create failed: " + JSON.stringify(data));
  return data;
}

async function updateDriveFile(id, mimeType, content) {
  const token = await accessToken();
  const res = await fetch("https://www.googleapis.com/upload/drive/v3/files/" + encodeURIComponent(id) + "?uploadType=media", {
    method: "PATCH",
    headers: {
      authorization: "Bearer " + token,
      "content-type": mimeType,
    },
    body: content,
  });
  const data = await res.json();
  if (!res.ok) throw new Error("Drive update failed: " + JSON.stringify(data));
  return data;
}

export async function publishPortfolioToDrive(portfolio) {
  const store = await driveStateStore();
  const state = (await store.get("files", { type: "json", consistency: "strong" })) || {};
  const outputs = [
    {
      key: "markdown",
      name: "GSC_Portfolio_Latest.md",
      mimeType: "text/markdown",
      content: portfolioMarkdown(portfolio),
    },
    {
      key: "json",
      name: "GSC_Portfolio_Latest.json",
      mimeType: "application/json",
      content: JSON.stringify(portfolio, null, 2),
    },
  ];
  const next = { ...state };
  for (const item of outputs) {
    if (state[item.key]?.id) {
      try {
        await updateDriveFile(state[item.key].id, item.mimeType, item.content);
        continue;
      } catch {
        delete next[item.key];
      }
    }
    const created = await uploadNewDriveFile(item.name, item.mimeType, item.content);
    next[item.key] = { id: created.id, name: created.name, webViewLink: created.webViewLink || null };
  }
  await store.setJSON("files", next);
  return next;
}

export async function syncAll() {
  const portfolio = await buildPortfolio();
  const drive = await publishPortfolioToDrive(portfolio);
  return { portfolio, drive };
}
