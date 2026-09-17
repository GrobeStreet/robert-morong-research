import { html, oauthUrl, getConfig } from "./_gsc.mjs";

export default async () => {
  const cfg = getConfig();
  if (!cfg.clientId || !cfg.clientSecret || !cfg.stateSecret) {
    return html(`<!doctype html><meta charset="utf-8"><title>GSC Connector Setup</title>
      <h1>Google Search Console connector is installed but not configured yet.</h1>
      <p>Missing one or more required environment variables.</p>
      <p>Return to the setup dashboard at <a href="/gsc/">/gsc/</a>.</p>`, 503);
  }
  return Response.redirect(oauthUrl(), 302);
};

export const config = { path: "/gsc/connect" };
