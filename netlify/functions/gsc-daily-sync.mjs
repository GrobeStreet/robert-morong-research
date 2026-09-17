import { syncAll } from "./_gsc.mjs";

export default async () => {
  try {
    const result = await syncAll();
    console.log("GSC daily sync complete", {
      generatedAt: result.portfolio.generatedAt,
      siteCount: result.portfolio.siteCount,
      totals: result.portfolio.totals,
    });
  } catch (error) {
    console.error("GSC daily sync failed", error);
    throw error;
  }
};
