import { getConfig, getSavedAuth, json } from "../lib/gsc.mjs";

export default async () => {
  const cfg = getConfig();
  let auth = null;
  try { auth = await getSavedAuth(); } catch {}
  return json({
    installed: true,
    googleClientConfigured: !!(cfg.clientId && cfg.clientSecret),
    stateSecretConfigured: !!cfg.stateSecret,
    redirectUri: cfg.redirectUri,
    allowedEmail: cfg.allowedEmail,
    connected: !!auth?.refresh_token,
    connectedEmail: auth?.email || null,
    lastAuthorizedAt: auth?.saved_at || null,
    requiredScopes: [
      "Search Console read-only",
      "Google Drive file access for connector-created snapshots"
    ]
  });
};

export const config = { path: "/gsc/status" };
