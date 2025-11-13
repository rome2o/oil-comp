# SEO Analysis Plan

## Objectives

1.  Assess the impact of the theme change on July 19th, 2025, on SEO performance.
2.  Evaluate the effectiveness of Allen's SEO efforts since February 12th, 2025, compared to the previous agency.

## Data Sources

*   **Ahrefs Reports:**
    *   `Overview - Hbnobulk-22-mar-2025.pdf`
    *   `Overview - Hbno-9-feb-2025.pdf`
    *   `Overview - Hbno-29-jun-2025.pdf`
    *   `Overview - Hbno-current-2025.pdf`
    *   `Overview - Hbnobulk-28-jun-2025.pdf`
    *   `Overview - Hbnobulk-current-2025.pdf`
    *   `hbnobulk.com-organic-keywords-subdomains-al_2025-10-22_19-38-50.csv`
    *   `hbnobulk.com-backlinks-subdomains_2025-10-22_19-38-16.csv`
*   **Google Analytics Reports:**
    *   `Pages and screens_ Page path and screen class.xlsx`
    *   `Traffic acquisition_ Session primary channel group (Default Channel Group).xlsx`
*   **Google Search Console Reports:**
    *   `https___hbno.com_-core-web-vitals-2025-10-22 (1).xlsx`
    *   `https___hbno.com_-core-web-vitals-2025-10-22.xlsx`
    *   `https___hbno.com_-Performance-on-Search-2025-10-22.xlsx`

## Analysis Phases

### Phase 1: Data Preparation & Initial Review
*   **Action:** Convert all relevant data (CSVs, XLSX) into a standardized, machine-readable format (e.g., pandas DataFrames in Python).
*   **Action:** Review PDF reports manually to extract key insights and data points not available in structured formats.
*   **Output:** Cleaned and structured datasets for each source.

### Phase 2: Baseline & Historical Performance Analysis
*   **Action:** Establish a baseline for SEO performance *before* Allen's involvement (prior to February 12th, 2025) using available historical data.
*   **Action:** Establish a baseline for SEO performance *before* the theme change (prior to July 19th, 2025).
*   **Output:** Defined baseline metrics for key SEO indicators (traffic, rankings, backlinks, core web vitals).

### Phase 3: Theme Change Impact Analysis
*   **Action:** Analyze Google Analytics data (traffic acquisition, pages & screens) to identify changes in user behavior and traffic patterns immediately following July 19th, 2025.
*   **Action:** Examine Google Search Console performance data (clicks, impressions, CTR, position) for any significant shifts post-theme change.
*   **Action:** Review Core Web Vitals data from GSC to assess any impact on site speed and user experience.
*   **Output:** Report on the positive, negative, or neutral impact of the theme change on SEO.

### Phase 4: Allen's SEO Efforts Analysis
*   **Action:** Compare SEO performance metrics (from Ahrefs, GA, GSC) from February 12th, 2025, onwards against the established baseline (pre-Allen).
*   **Action:** Analyze organic keyword performance and backlink profile changes (from Ahrefs) to evaluate the effectiveness of strategies implemented by Allen.
*   **Action:** Correlate specific SEO activities (if documented) with observed performance changes.
*   **Output:** Assessment of the effectiveness of Allen's SEO efforts, highlighting areas of success and areas needing improvement.

### Phase 5: Reporting & Recommendations
*   **Action:** Consolidate findings from all phases into a comprehensive SEO analysis report.
*   **Action:** Provide actionable recommendations for future SEO strategy, addressing identified issues and capitalizing on opportunities.
*   **Output:** Executive summary, detailed findings, and a prioritized list of recommendations.

## Tools

*   Python (Pandas for data manipulation, Matplotlib/Seaborn for visualization)
*   Manual review for PDF reports and qualitative insights.

## Deliverables

*   Individual analysis notes for each data file (created in `seo/analysis_notes/`).
*   Comprehensive SEO Analysis Report (Markdown or PDF).
*   Prioritized list of actionable SEO recommendations.
