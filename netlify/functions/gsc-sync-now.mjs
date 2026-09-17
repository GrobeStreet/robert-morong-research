import { hasValidSession, json, syncAll } from "../lib/gsc.mjs";

export default async (req) => {
  if (!hasValidSession(req)) return json({ error: "Not authorized." }, 401);
  try {
    const result = await syncAll();
    return json({
      ok: true,
      generatedAt: result.portfolio.generatedAt,
      siteCount: result.portfolio.siteCount,
      totals: result.portfolio.totals,
      driveFiles: result.drive,
    });
  } catch (error) {
    return json({ ok: false, error: String(error?.message || error) }, 500);
  }
};

export const config = { path: "/gsc/sync" };
