# 3 Analysis #2: Allen's Performance vs Previous Agency

### 10.3 Analysis #2: Allen's Performance vs Previous Agency

```python
# Prepare comparison data
comparison_summary = pd.DataFrame({
    'Metric': ['Average Daily Clicks', 'Average Daily Impressions', 'Average CTR (%)', 'Average Position'],
    'Previous Agency': [
        previous_agency['Clicks'].mean(),
        previous_agency['Impressions'].mean(),
        previous_agency['CTR'].mean() * 100,
        previous_agency['Position'].mean()
    ],
    'Allen (Pre-Theme)': [
        allen_pre_theme['Clicks'].mean(),
        allen_pre_theme['Impressions'].mean(),
        allen_pre_theme['CTR'].mean() * 100,
        allen_pre_theme['Position'].mean()
    ]
})
comparison_summary['% Change'] = ((comparison_summary['Allen (Pre-Theme)'] - comparison_summary['Previous Agency']) 
                                   / comparison_summary['Previous Agency'] * 100).round(2)

data_context = f"""
Performance Comparison: Previous Agency vs Allen (Pre-Theme Change)

Previous Agency Period: {previous_agency['Date'].min().date()} to {previous_agency['Date'].max().date()} ({len(previous_agency)} days)
Allen's Period: {allen_pre_theme['Date'].min().date()} to {allen_pre_theme['Date'].max().date()} ({len(allen_pre_theme)} days)

Summary Metrics:
{comparison_summary.to_string(index=False)}

Statistical Significance Results:
{allen_comparison.to_string()}
"""

prompt = """
You are an expert SEO consultant evaluating the performance of a new SEO manager (Allen) compared to the previous agency.

Allen started on February 12, 2025, and this analysis covers his work BEFORE the theme change (to isolate his impact).

Context:
- The oil company was previously using an external SEO agency
- Allen was hired to manage SEO in-house
- This is a critical evaluation to determine ROI and effectiveness

Please provide:
1. **Overall Performance Assessment**: How did Allen perform compared to the previous agency? Grade his performance (A-F).
2. **Strengths**: What did Allen do particularly well?
3. **Areas for Improvement**: Where could Allen's strategy be enhanced?
4. **Competitive Analysis**: How do these metrics compare to industry benchmarks for B2B oil companies?
5. **ROI Evaluation**: Based on these metrics, is the in-house approach working?
6. **Strategic Recommendations**: What should Allen focus on for the next quarter?

Be honest but constructive in your assessment.
"""

print("🔍 Analyzing Allen's performance with Gemini AI...")
response = analyze_with_gemini(prompt, data_context)
display_ai_response("Allen's Performance Evaluation", response)
```


---

[← Back to Index](./00_index.md)
