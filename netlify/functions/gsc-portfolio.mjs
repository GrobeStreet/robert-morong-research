import { hasValidSession, latestPortfolio, json } from "./_gsc.mjs";

export default async (req) => {
  if (!hasValidSession(req)) return json({ error: "Not authorized. Open /gsc/connect first." }, 401);
  const data = await latestPortfolio();
  if (!data) return json({ error: "No snapshot exists yet. Run a manual sync from /gsc/." }, 404);
  return json(data);
};

export const config = { path: "/gsc/portfolio" };
