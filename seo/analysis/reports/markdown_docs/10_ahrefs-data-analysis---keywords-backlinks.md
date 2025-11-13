# Ahrefs Data Analysis - Keywords & Backlinks

## 8. Ahrefs Data Analysis - Keywords & Backlinks

```python
# Load Ahrefs data
print("Loading Ahrefs datasets...\n")

# Organic Keywords
ahrefs_keywords = pd.read_csv('../../analysis/processed_data/ahrefs_organic_keywords.csv')
print(f"✓ Ahrefs Organic Keywords: {len(ahrefs_keywords):,} keywords")

# Backlinks
ahrefs_backlinks = pd.read_csv('../../analysis/processed_data/ahrefs_backlinks.csv')
print(f"✓ Ahrefs Backlinks: {len(ahrefs_backlinks):,} backlinks")

print("\n" + "="*50)
print("Keyword Rankings Distribution:")
print("="*50)

# Analyze keyword positions
position_breakdown = pd.cut(ahrefs_keywords['Current position'], 
                            bins=[0, 3, 10, 20, 50, 100], 
                            labels=['Top 3', 'Top 10', 'Top 20', 'Top 50', 'Top 100'])
print(position_breakdown.value_counts().sort_index())

# Traffic analysis
print("\n" + "="*50)
print("Traffic Statistics:")
print("="*50)
print(f"Total Current Organic Traffic: {ahrefs_keywords['Current organic traffic'].sum():,.0f}")
print(f"Average Traffic per Keyword: {ahrefs_keywords['Current organic traffic'].mean():.2f}")

# Top performing keywords
print("\n" + "="*50)
print("Top 10 Keywords by Traffic:")
print("="*50)
top_traffic = ahrefs_keywords.nlargest(10, 'Current organic traffic')[
    ['Keyword', 'Current position', 'Volume', 'Current organic traffic', 'Branded']
]
print(top_traffic.to_string(index=False))

print("\n✓ Ahrefs data loaded successfully")
```

**Output:**

```
Loading Ahrefs datasets...

✓ Ahrefs Organic Keywords: 14,293 keywords
✓ Ahrefs Backlinks: 2,908 backlinks

==================================================
Keyword Rankings Distribution:
==================================================
Current position
Top 3       681
Top 10     2061
Top 20     1413
Top 50     1035
Top 100     628
Name: count, dtype: int64

==================================================
Traffic Statistics:
==================================================
Total Current Organic Traffic: 10,353
Average Traffic per Keyword: 1.77

==================================================
Top 10 Keywords by Traffic:
==================================================
                               Keyword  Current position  Volume  Current organic traffic  Branded
                                  hbno               1.0     450                    312.0     True
   how to dilute tea tree oil for dogs               1.0     300                    127.0    False
             fall essential oil blends               9.0    4600                    125.0    False
          can dogs have black seed oil               2.0     300                    114.0    False
               black seed oil for dogs               1.0     300                    109.0    False
            best body oil for dry skin               6.0    1300                    102.0    False
cheapest carrier oil for reed diffuser               1.0     200                     77.0    False
                  helichrysum benefits               9.0    3300                     76.0    False
             canola oil vs coconut oil               5.0     800                     73.0    False
बालों में सरसों का तेल लगाने के नुकसान               9.0    1700                     67.0    False

✓ Ahrefs data loaded successfully

```

```python
# Visualize keyword distribution and performance
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Ahrefs Keyword Performance Analysis', fontsize=16, fontweight='bold')

# 1. Position Distribution
position_dist = ahrefs_keywords['Current position'].value_counts().sort_index()[:20]
axes[0, 0].bar(position_dist.index, position_dist.values, color='#4ecdc4')
axes[0, 0].set_xlabel('Search Position', fontsize=12)
axes[0, 0].set_ylabel('Number of Keywords', fontsize=12)
axes[0, 0].set_title('Top 20 Position Distribution', fontsize=14, fontweight='bold')

# 2. Traffic by Position Category
position_categories = pd.cut(ahrefs_keywords['Current position'], 
                             bins=[0, 3, 10, 20, 50, 100], 
                             labels=['Top 3', 'Top 10', 'Top 20', 'Top 50', 'Top 100'])
traffic_by_position = ahrefs_keywords.groupby(position_categories)['Current organic traffic'].sum()
axes[0, 1].bar(range(len(traffic_by_position)), traffic_by_position.values, 
               color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#dfe6e9'])
axes[0, 1].set_xticks(range(len(traffic_by_position)))
axes[0, 1].set_xticklabels(traffic_by_position.index, rotation=45)
axes[0, 1].set_ylabel('Total Traffic', fontsize=12)
axes[0, 1].set_title('Traffic Distribution by Position Range', fontsize=14, fontweight='bold')

# 3. Branded vs Non-Branded Traffic
branded_traffic = ahrefs_keywords.groupby('Branded')['Current organic traffic'].sum()
axes[1, 0].pie(branded_traffic.values, labels=['Non-Branded', 'Branded'], 
               autopct='%1.1f%%', colors=['#4ecdc4', '#ff6b6b'], startangle=90)
axes[1, 0].set_title('Branded vs Non-Branded Traffic', fontsize=14, fontweight='bold')

# 4. Keyword Intent Distribution
intent_cols = ['Navigational', 'Informational', 'Commercial', 'Transactional']
intent_data = []
for col in intent_cols:
    if col in ahrefs_keywords.columns:
        count = ahrefs_keywords[ahrefs_keywords[col] == True].shape[0]
        intent_data.append(count)

if intent_data:
    axes[1, 1].bar(intent_cols, intent_data, color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'])
    axes[1, 1].set_ylabel('Number of Keywords', fontsize=12)
    axes[1, 1].set_title('Keyword Intent Distribution', fontsize=14, fontweight='bold')
    axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('../../analysis/visualizations/ahrefs_keyword_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Keyword visualizations saved")
```

**Output:**

*[Chart/Visualization displayed]*

```
✓ Keyword visualizations saved

```

```python
# Backlink Analysis
print("="*50)
print("Backlink Profile Analysis")
print("="*50)

# Domain Rating distribution
print("\nDomain Rating Statistics:")
print(ahrefs_backlinks['Domain rating'].describe())

# High-quality backlinks (DR > 50)
high_quality = ahrefs_backlinks[ahrefs_backlinks['Domain rating'] > 50]
print(f"\nHigh-Quality Backlinks (DR > 50): {len(high_quality):,} ({len(high_quality)/len(ahrefs_backlinks)*100:.1f}%)")

# Dofollow vs Nofollow
nofollow_count = ahrefs_backlinks['Nofollow'].sum()
dofollow_count = len(ahrefs_backlinks) - nofollow_count
print(f"\nDofollow Links: {dofollow_count:,} ({dofollow_count/len(ahrefs_backlinks)*100:.1f}%)")
print(f"Nofollow Links: {nofollow_count:,} ({nofollow_count/len(ahrefs_backlinks)*100:.1f}%)")

# Link discovery timeline
ahrefs_backlinks['First seen'] = pd.to_datetime(ahrefs_backlinks['First seen'])
ahrefs_backlinks['Month'] = ahrefs_backlinks['First seen'].dt.to_period('M')

# Group by month to see acquisition rate
monthly_backlinks = ahrefs_backlinks.groupby('Month').size()

print("\n" + "="*50)
print("Recent Backlink Acquisition (Last 6 Months):")
print("="*50)
print(monthly_backlinks.tail(6))

# Visualize backlink metrics
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Backlink Profile Analysis', fontsize=16, fontweight='bold')

# 1. Domain Rating Distribution
axes[0].hist(ahrefs_backlinks['Domain rating'].dropna(), bins=20, color='#4ecdc4', edgecolor='black')
axes[0].axvline(ahrefs_backlinks['Domain rating'].mean(), color='red', linestyle='--', 
                label=f'Mean: {ahrefs_backlinks["Domain rating"].mean():.1f}')
axes[0].set_xlabel('Domain Rating', fontsize=12)
axes[0].set_ylabel('Number of Backlinks', fontsize=12)
axes[0].set_title('Domain Rating Distribution', fontsize=14, fontweight='bold')
axes[0].legend()

# 2. Dofollow vs Nofollow
link_types = ['Dofollow', 'Nofollow']
link_counts = [dofollow_count, nofollow_count]
axes[1].pie(link_counts, labels=link_types, autopct='%1.1f%%', 
            colors=['#4ecdc4', '#ff6b6b'], startangle=90)
axes[1].set_title('Link Type Distribution', fontsize=14, fontweight='bold')

# 3. Monthly Backlink Acquisition
recent_months = monthly_backlinks.tail(12)
axes[2].plot(range(len(recent_months)), recent_months.values, marker='o', 
             linewidth=2, markersize=8, color='#4ecdc4')
axes[2].set_xticks(range(len(recent_months)))
axes[2].set_xticklabels([str(m) for m in recent_months.index], rotation=45, ha='right')
axes[2].set_ylabel('New Backlinks', fontsize=12)
axes[2].set_title('Monthly Backlink Acquisition (Last 12 Months)', fontsize=14, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../../analysis/visualizations/backlink_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Backlink analysis complete")
```

**Output:**

```
==================================================
Backlink Profile Analysis
==================================================

Domain Rating Statistics:
count    2908.000000
mean       30.130915
std        27.075805
min         0.000000
25%         3.400000
50%        26.000000
75%        52.000000
max        96.000000
Name: Domain rating, dtype: float64

High-Quality Backlinks (DR > 50): 775 (26.7%)

Dofollow Links: 1,010 (34.7%)
Nofollow Links: 1,898 (65.3%)

==================================================
Recent Backlink Acquisition (Last 6 Months):
==================================================
Month
2025-05    228
2025-06    106
2025-07    149
2025-08    102
2025-09    143
2025-10     85
Freq: M, dtype: int64

```

*[Chart/Visualization displayed]*

```

✓ Backlink analysis complete

```

```python
# Generate comprehensive summary including Ahrefs data
summary = []
summary.append("# SEO Analysis Executive Summary")
summary.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
summary.append("\n## Data Overview")
summary.append(f"- Analysis Period: {gsc_dates['Date'].min().date()} to {gsc_dates['Date'].max().date()}")
summary.append(f"- Total Days Analyzed: {len(gsc_dates)}")
summary.append(f"- Total Clicks: {gsc_dates['Clicks'].sum():,}")
summary.append(f"- Total Impressions: {gsc_dates['Impressions'].sum():,}")

summary.append("\n## Ahrefs Metrics")
summary.append(f"- Total Tracked Keywords: {len(ahrefs_keywords):,}")
summary.append(f"- Keywords in Top 10: {len(ahrefs_keywords[ahrefs_keywords['Current position'] <= 10]):,}")
summary.append(f"- Current Organic Traffic: {ahrefs_keywords['Current organic traffic'].sum():,.0f}")
summary.append(f"- Total Backlinks: {len(ahrefs_backlinks):,}")
summary.append(f"- Average Domain Rating: {ahrefs_backlinks['Domain rating'].mean():.1f}")
summary.append(f"- Dofollow Links: {(len(ahrefs_backlinks) - ahrefs_backlinks['Nofollow'].sum()):,} ({((len(ahrefs_backlinks) - ahrefs_backlinks['Nofollow'].sum())/len(ahrefs_backlinks)*100):.1f}%)")

summary.append("\n## Theme Change Impact (July 19, 2025)")
for metric in metrics:
    change = theme_impact.loc[metric, '% Change']
    direction = "📈 Improved" if change > 0 and metric != 'Position' else "📉 Declined" if change < 0 and metric != 'Position' else "→ Stable"
    if metric == 'Position':
        direction = "📈 Improved" if change < 0 else "📉 Declined" if change > 0 else "→ Stable"
    summary.append(f"- {metric}: {direction} by {abs(change):.2f}%")

summary.append("\n## Allen's Performance (vs Previous Agency)")
for metric in metrics:
    change = allen_comparison.loc[metric, '% Change']
    direction = "📈 Improved" if change > 0 and metric != 'Position' else "📉 Declined" if change < 0 and metric != 'Position' else "→ Stable"
    if metric == 'Position':
        direction = "📈 Improved" if change < 0 else "📉 Declined" if change > 0 else "→ Stable"
    summary.append(f"- {metric}: {direction} by {abs(change):.2f}%")

summary.append("\n## Keyword Performance Insights")
branded_traffic = ahrefs_keywords[ahrefs_keywords['Branded'] == True]['Current organic traffic'].sum()
total_traffic = ahrefs_keywords['Current organic traffic'].sum()
summary.append(f"- Branded Traffic: {branded_traffic:,.0f} ({branded_traffic/total_traffic*100:.1f}%)")
summary.append(f"- Non-Branded Traffic: {total_traffic - branded_traffic:,.0f} ({(total_traffic - branded_traffic)/total_traffic*100:.1f}%)")
top_traffic_keyword = ahrefs_keywords.nlargest(1, 'Current organic traffic').iloc[0]
summary.append(f"- Top Performing Keyword: '{top_traffic_keyword['Keyword']}' (Traffic: {top_traffic_keyword['Current organic traffic']:.0f})")

summary.append("\n## Recommendations")
summary.append("1. Monitor theme change impact closely and address any technical issues")
summary.append("2. Continue building on Allen's positive momentum in traffic and engagement")
summary.append("3. Focus on improving non-branded keyword rankings for sustainable growth")
summary.append("4. Maintain backlink acquisition pace and focus on high-DR domains")
summary.append("5. Optimize underperforming keywords in positions 11-20 to break into top 10")

summary_text = '\n'.join(summary)
print(summary_text)

# Save summary
with open('../../analysis/reports/executive_summary.md', 'w') as f:
    f.write(summary_text)

print("\n" + "="*50)
print("✓ Executive summary saved to: analysis/reports/executive_summary.md")
print("✓ Analysis complete!")
print("\nGenerated visualizations:")
print("- analysis/visualizations/period_comparison.png")
print("- analysis/visualizations/top_queries.png")
print("- analysis/visualizations/ahrefs_keyword_analysis.png")
print("- analysis/visualizations/backlink_analysis.png")
```

**Output:**

```
# SEO Analysis Executive Summary
Generated: 2025-10-22 21:27:58

## Data Overview
- Analysis Period: 2024-07-08 to 2025-10-21
- Total Days Analyzed: 471
- Total Clicks: 27,582
- Total Impressions: 2,594,505

## Ahrefs Metrics
- Total Tracked Keywords: 14,293
- Keywords in Top 10: 2,742
- Current Organic Traffic: 10,353
- Total Backlinks: 2,908
- Average Domain Rating: 30.1
- Dofollow Links: 1,010 (34.7%)

## Theme Change Impact (July 19, 2025)
- Clicks: 📈 Improved by 21.80%
- Impressions: 📈 Improved by 10.05%
- CTR: 📈 Improved by 10.89%
- Position: 📈 Improved by 3.65%

## Allen's Performance (vs Previous Agency)
- Clicks: 📈 Improved by 222.69%
- Impressions: 📈 Improved by 627.40%
- CTR: 📉 Declined by 78.12%
- Position: 📈 Improved by 18.54%

## Keyword Performance Insights
- Branded Traffic: 613 (5.9%)
- Non-Branded Traffic: 9,740 (94.1%)
- Top Performing Keyword: 'hbno' (Traffic: 312)

## Recommendations
1. Monitor theme change impact closely and address any technical issues
2. Continue building on Allen's positive momentum in traffic and engagement
3. Focus on improving non-branded keyword rankings for sustainable growth
4. Maintain backlink acquisition pace and focus on high-DR domains
5. Optimize underperforming keywords in positions 11-20 to break into top 10

==================================================
✓ Executive summary saved to: analysis/reports/executive_summary.md
✓ Analysis complete!

Generated visualizations:
- analysis/visualizations/period_comparison.png
- analysis/visualizations/top_queries.png
- analysis/visualizations/ahrefs_keyword_analysis.png
- analysis/visualizations/backlink_analysis.png

```


---

[← Back to Index](./00_index.md)
