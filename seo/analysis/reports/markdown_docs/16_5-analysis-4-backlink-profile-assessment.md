# 5 Analysis #4: Backlink Profile Assessment

### 10.5 Analysis #4: Backlink Profile Assessment

```python
# Prepare backlink analysis
backlink_summary = {
    'Total Backlinks': len(ahrefs_backlinks),
    'Average Domain Rating': ahrefs_backlinks['Domain rating'].mean(),
    'Median Domain Rating': ahrefs_backlinks['Domain rating'].median(),
    'High Quality Links (DR>50)': len(ahrefs_backlinks[ahrefs_backlinks['Domain rating'] > 50]),
    'Dofollow Links': len(ahrefs_backlinks) - ahrefs_backlinks['Nofollow'].sum(),
    'Nofollow Links': ahrefs_backlinks['Nofollow'].sum(),
    'Dofollow %': ((len(ahrefs_backlinks) - ahrefs_backlinks['Nofollow'].sum()) / len(ahrefs_backlinks) * 100)
}

# Top referring domains
top_domains = ahrefs_backlinks.nlargest(30, 'Domain rating')[
    ['Referring page URL', 'Domain rating', 'Nofollow', 'First seen']
]

# Monthly acquisition
monthly_acquisition = ahrefs_backlinks.groupby(
    ahrefs_backlinks['First seen'].dt.to_period('M')
).size().tail(12)

data_context = f"""
Backlink Profile Summary:
{pd.Series(backlink_summary).to_string()}

Domain Rating Distribution:
{ahrefs_backlinks['Domain rating'].describe().to_string()}

Top 30 Referring Domains by DR:
{top_domains.to_string(index=False)}

Monthly Backlink Acquisition (Last 12 Months):
{monthly_acquisition.to_string()}
"""

prompt = """
You are an expert link building strategist. Analyze this backlink profile for an oil company website.

Analysis Requirements:
1. **Profile Quality Assessment**: How healthy is this backlink profile? What's the overall grade (A-F)?
2. **Authority Analysis**: Is the average domain rating competitive for the industrial/oil sector?
3. **Link Type Balance**: Evaluate the dofollow/nofollow ratio - is it natural or concerning?
4. **Acquisition Velocity**: Analyze the monthly acquisition pattern - is it sustainable?
5. **Risk Factors**: Identify any red flags (toxic links, unnatural patterns, over-optimization)
6. **Competitive Benchmarking**: How does this profile compare to typical B2B industrial sites?
7. **Opportunity Analysis**: What types of high-quality links are missing?

Provide:
- Overall backlink health score (1-10)
- 5 specific link building recommendations
- 3 immediate actions to strengthen the profile
- Warning signs to monitor
"""

print("🔍 Analyzing backlink profile with Gemini AI...")
response = analyze_with_gemini(prompt, data_context)
display_ai_response("Backlink Profile Assessment", response)
```


---

[← Back to Index](./00_index.md)
