# Theme Change Impact Analysis

## 5. Theme Change Impact Analysis

```python
# Define pre and post theme periods (30 days each for fair comparison)
pre_theme_start = theme_change_date - timedelta(days=30)
post_theme_end = theme_change_date + timedelta(days=30)

pre_theme = gsc_dates[(gsc_dates['Date'] >= pre_theme_start) & (gsc_dates['Date'] < theme_change_date)]
post_theme = gsc_dates[(gsc_dates['Date'] >= theme_change_date) & (gsc_dates['Date'] <= post_theme_end)]

print("Theme Change Impact Analysis")
print("="*50)
print(f"Pre-Theme Period: {pre_theme_start.date()} to {(theme_change_date - timedelta(days=1)).date()} ({len(pre_theme)} days)")
print(f"Post-Theme Period: {theme_change_date.date()} to {post_theme_end.date()} ({len(post_theme)} days)")
print()

# Calculate changes
metrics = ['Clicks', 'Impressions', 'CTR', 'Position']
theme_impact = pd.DataFrame({
    'Pre-Theme': pre_theme[metrics].mean(),
    'Post-Theme': post_theme[metrics].mean()
})

theme_impact['Change'] = theme_impact['Post-Theme'] - theme_impact['Pre-Theme']
theme_impact['% Change'] = ((theme_impact['Post-Theme'] - theme_impact['Pre-Theme']) / theme_impact['Pre-Theme'] * 100).round(2)

print("\nMetric Changes After Theme Implementation:")
print(theme_impact)

# Statistical significance testing
print("\n" + "="*50)
print("Statistical Significance Tests (t-tests):")
print("="*50)

for metric in metrics:
    t_stat, p_value = stats.ttest_ind(pre_theme[metric], post_theme[metric])
    significance = "✓ SIGNIFICANT" if p_value < 0.05 else "✗ Not significant"
    print(f"\n{metric}:")
    print(f"  t-statistic: {t_stat:.3f}")
    print(f"  p-value: {p_value:.4f}")
    print(f"  Result: {significance}")
```

**Output:**

```
Theme Change Impact Analysis
==================================================
Pre-Theme Period: 2025-06-19 to 2025-07-18 (30 days)
Post-Theme Period: 2025-07-19 to 2025-08-18 (31 days)


Metric Changes After Theme Implementation:
                Pre-Theme    Post-Theme       Change  % Change
Clicks          99.500000    121.193548    21.693548     21.80
Impressions  13186.533333  14511.741935  1325.208602     10.05
CTR              0.007567      0.008390     0.000824     10.89
Position        24.125000     23.243871    -0.881129     -3.65

==================================================
Statistical Significance Tests (t-tests):
==================================================

Clicks:
  t-statistic: -4.713
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

Impressions:
  t-statistic: -4.472
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

CTR:
  t-statistic: -2.438
  p-value: 0.0178
  Result: ✓ SIGNIFICANT

Position:
  t-statistic: 2.588
  p-value: 0.0121
  Result: ✓ SIGNIFICANT

```


---

[← Back to Index](./00_index.md)
