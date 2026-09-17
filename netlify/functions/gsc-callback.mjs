import { exchangeCode, fetchUserEmail, getConfig, html, makeSessionCookie, saveAuth, verifyState } from "./_gsc.mjs";

export default async (req) => {
  try {
    const url = new URL(req.url);
    const code = url.searchParams.get("code");
    const state = url.searchParams.get("state");
    const error = url.searchParams.get("error");
    if (error) return html("<h1>Google authorization was not completed.</h1><p>" + error + "</p>", 400);
    if (!code || !verifyState(state)) return html("<h1>Invalid or expired OAuth callback.</h1>", 400);

    const tokens = await exchangeCode(code);
    const email = await fetchUserEmail(tokens.access_token);
    const cfg = getConfig();
    if (email !== cfg.allowedEmail) {
      return html("<h1>Wrong Google account.</h1><p>Please authorize with " + cfg.allowedEmail + ".</p>", 403);
    }
    await saveAuth(tokens, email);
    return html(`<!doctype html><meta charset="utf-8"><title>GSC Connected</title>
      <h1>Connected.</h1>
      <p>Google Search Console access is now stored securely in Netlify Blobs for <strong>${email}</strong>.</p>
      <p><a href="/gsc/">Open the GSC dashboard</a></p>`, 200, { "set-cookie": makeSessionCookie(email) });
  } catch (error) {
    return html("<h1>Connection failed.</h1><pre>" + String(error?.message || error).replace(/[&<>]/g, "") + "</pre>", 500);
  }
};

export const config = { path: "/gsc/callback" };
