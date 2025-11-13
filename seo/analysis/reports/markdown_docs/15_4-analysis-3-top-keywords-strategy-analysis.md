# 4 Analysis #3: Top Keywords Strategy Analysis

### 10.4 Analysis #3: Top Keywords Strategy Analysis

```python
# Prepare keyword analysis data
top_keywords = ahrefs_keywords.nlargest(50, 'Current organic traffic')[
    ['Keyword', 'Current position', 'Volume', 'Current organic traffic', 'Branded', 
     'Navigational', 'Informational', 'Commercial', 'Transactional']
]

# Additional keyword metrics
keyword_summary = {
    'Total Keywords': len(ahrefs_keywords),
    'Top 3 Rankings': len(ahrefs_keywords[ahrefs_keywords['Current position'] <= 3]),
    'Top 10 Rankings': len(ahrefs_keywords[ahrefs_keywords['Current position'] <= 10]),
    'Branded Keywords': len(ahrefs_keywords[ahrefs_keywords['Branded'] == True]),
    'Non-Branded Keywords': len(ahrefs_keywords[ahrefs_keywords['Branded'] == False]),
    'Total Organic Traffic': ahrefs_keywords['Current organic traffic'].sum(),
    'Branded Traffic %': (ahrefs_keywords[ahrefs_keywords['Branded'] == True]['Current organic traffic'].sum() / 
                         ahrefs_keywords['Current organic traffic'].sum() * 100)
}

data_context = f"""
Top 50 Keywords by Traffic:
{top_keywords.to_string(index=False)}

Overall Keyword Portfolio Summary:
{pd.Series(keyword_summary).to_string()}

Position Distribution:
{pd.cut(ahrefs_keywords['Current position'], bins=[0, 3, 10, 20, 50, 100], labels=['Top 3', 'Top 10', 'Top 20', 'Top 50', 'Top 100']).value_counts().sort_index().to_string()}
"""

prompt = """
You are an expert SEO strategist specializing in B2B industrial sectors. Analyze this keyword portfolio for an oil company (hbno.com / hbnobulk.com).

Focus Areas:
1. **Keyword Portfolio Health**: Assess the overall quality and diversity of the keyword portfolio
2. **Branded vs Non-Branded Balance**: Is the reliance on branded traffic healthy or concerning?
3. **Intent Analysis**: Evaluate the mix of navigational, informational, commercial, and transactional keywords
4. **Quick Win Opportunities**: Identify keywords in positions 4-10 that could be pushed to top 3
5. **Content Gaps**: What keyword opportunities are being missed based on the current portfolio?
6. **Competitive Vulnerability**: Which high-traffic keywords are at risk (positions 5+)?
7. **Long-tail Strategy**: Should they focus more on long-tail keywords?

Provide:
- 3-5 immediate action items for keyword optimization
- 3-5 strategic recommendations for keyword expansion
- Risk assessment: what happens if top branded keywords lose rankings?
"""

print("🔍 Analyzing keyword strategy with Gemini AI...")
response = analyze_with_gemini(prompt, data_context)
display_ai_response("Keyword Strategy Analysis", response)
```


---

[← Back to Index](./00_index.md)
