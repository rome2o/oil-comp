# 2 Analysis #1: Theme Change Impact Deep Dive

### 10.2 Analysis #1: Theme Change Impact Deep Dive

```python
# Prepare theme change data
theme_data = pd.concat([
    pre_theme.assign(Period='Pre-Theme'),
    post_theme.assign(Period='Post-Theme')
])

data_context = prepare_data_context(
    theme_data, 
    "SEO Performance Data: 30 days before and after theme change (July 19, 2025)",
    max_rows=30
)

prompt = """
You are an expert SEO analyst. Analyze this data comparing website performance before and after a major theme change on July 19, 2025.

Key metrics to analyze:
- Clicks: user clicks from search results
- Impressions: how often the site appeared in search
- CTR: click-through rate (clicks/impressions)
- Position: average ranking position (lower is better)

Please provide:
1. **Key Findings**: What are the most significant changes? Are they positive or negative?
2. **Root Cause Analysis**: What might have caused these changes? Consider technical SEO factors.
3. **Trend Patterns**: Are there any concerning trends or patterns?
4. **Risk Assessment**: What are the potential risks if these trends continue?
5. **Actionable Recommendations**: Provide 5-7 specific, technical recommendations to address any issues or capitalize on improvements.

Format your response with clear sections and bullet points.
"""

print("🔍 Analyzing theme change impact with Gemini AI...")
response = analyze_with_gemini(prompt, data_context)
display_ai_response("Theme Change Impact Analysis", response)
```


---

[← Back to Index](./00_index.md)
