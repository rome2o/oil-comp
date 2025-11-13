# 6 Analysis #5: Strategic SEO Roadmap (Next 90 Days)

### 10.6 Analysis #5: Strategic SEO Roadmap (Next 90 Days)

```python
# Compile all key insights for strategic planning
strategic_context = f"""
COMPREHENSIVE SEO SITUATION ANALYSIS
====================================

1. THEME CHANGE IMPACT (July 19, 2025):
{theme_impact.to_string()}

2. ALLEN'S PERFORMANCE VS PREVIOUS AGENCY:
{allen_comparison.to_string()}

3. CURRENT TRAFFIC METRICS:
- Total Keywords Ranking: {len(ahrefs_keywords):,}
- Keywords in Top 10: {len(ahrefs_keywords[ahrefs_keywords['Current position'] <= 10]):,}
- Current Organic Traffic: {ahrefs_keywords['Current organic traffic'].sum():,.0f}
- Total Backlinks: {len(ahrefs_backlinks):,}
- Average Domain Rating: {ahrefs_backlinks['Domain rating'].mean():.1f}

4. TOP PERFORMING QUERIES (from GSC):
{gsc_queries.nlargest(10, 'Clicks')[['Top queries', 'Clicks', 'Position']].to_string(index=False)}

5. KEYWORD DISTRIBUTION:
{pd.cut(ahrefs_keywords['Current position'], bins=[0, 3, 10, 20, 50, 100], labels=['Top 3', 'Top 10', 'Top 20', 'Top 50', 'Top 100']).value_counts().sort_index().to_string()}

6. RECENT TRENDS (Last 30 Days):
- Average Daily Clicks: {gsc_dates.tail(30)['Clicks'].mean():.1f}
- Average Daily Impressions: {gsc_dates.tail(30)['Impressions'].mean():.1f}
- Average CTR: {gsc_dates.tail(30)['CTR'].mean():.3%}
- Average Position: {gsc_dates.tail(30)['Position'].mean():.2f}
"""

prompt = """
You are a senior SEO strategist creating a 90-day action plan for an oil company website (hbno.com / hbnobulk.com).

Context:
- Recent theme change has impacted performance
- In-house SEO manager (Allen) needs clear direction
- B2B industrial sector with long sales cycles
- Need to balance quick wins with long-term growth

Create a detailed 90-day roadmap with:

**MONTH 1 (Days 1-30): Stabilization & Quick Wins**
- List 5-7 specific tasks with priority (P0/P1/P2)
- Focus on addressing theme change issues
- Include measurable KPIs for each task

**MONTH 2 (Days 31-60): Growth Initiatives**
- List 5-7 specific tasks with priority
- Focus on content and keyword expansion
- Include measurable KPIs for each task

**MONTH 3 (Days 61-90): Scale & Optimize**
- List 5-7 specific tasks with priority
- Focus on link building and authority
- Include measurable KPIs for each task

**Success Metrics:**
Define what success looks like at the end of 90 days (specific numbers)

**Resource Requirements:**
What tools, budget, or team resources are needed?

**Risk Mitigation:**
What could go wrong and how to prevent it?

Be specific, actionable, and realistic. Each task should be something Allen can start working on immediately.
"""

print("🔍 Creating strategic roadmap with Gemini AI...")
response = analyze_with_gemini(prompt, strategic_context)
display_ai_response("90-Day Strategic SEO Roadmap", response)
```


---

[← Back to Index](./00_index.md)
