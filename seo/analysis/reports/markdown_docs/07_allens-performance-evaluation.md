# Allen's Performance Evaluation

## 6. Allen's Performance Evaluation

```python
# Compare Previous Agency vs Allen (pre-theme)
previous_agency = gsc_dates[gsc_dates['Period'] == 'Previous Agency']
allen_pre_theme = gsc_dates[gsc_dates['Period'] == 'Allen Pre-Theme']

print("Allen's Performance Evaluation")
print("="*50)
print(f"Previous Agency: {len(previous_agency)} days of data")
print(f"Allen Pre-Theme: {len(allen_pre_theme)} days of data")
print()

# Calculate comparison
allen_comparison = pd.DataFrame({
    'Previous Agency': previous_agency[metrics].mean(),
    'Allen (Pre-Theme)': allen_pre_theme[metrics].mean()
})

allen_comparison['Change'] = allen_comparison['Allen (Pre-Theme)'] - allen_comparison['Previous Agency']
allen_comparison['% Change'] = ((allen_comparison['Allen (Pre-Theme)'] - allen_comparison['Previous Agency']) / allen_comparison['Previous Agency'] * 100).round(2)

print("\nPerformance Comparison:")
print(allen_comparison)

# Statistical significance
print("\n" + "="*50)
print("Statistical Significance Tests:")
print("="*50)

for metric in metrics:
    if len(previous_agency) > 0 and len(allen_pre_theme) > 0:
        t_stat, p_value = stats.ttest_ind(previous_agency[metric], allen_pre_theme[metric])
        significance = "✓ SIGNIFICANT" if p_value < 0.05 else "✗ Not significant"
        print(f"\n{metric}:")
        print(f"  t-statistic: {t_stat:.3f}")
        print(f"  p-value: {p_value:.4f}")
        print(f"  Result: {significance}")
```

**Output:**

```
Allen's Performance Evaluation
==================================================
Previous Agency: 219 days of data
Allen Pre-Theme: 157 days of data


Performance Comparison:
             Previous Agency  Allen (Pre-Theme)       Change  % Change
Clicks             21.260274          68.605096    47.344822    222.69
Impressions       939.853881        6836.541401  5896.687520    627.40
CTR                 0.054731           0.011975    -0.042756    -78.12
Position           34.125845          27.799682    -6.326163    -18.54

==================================================
Statistical Significance Tests:
==================================================

Clicks:
  t-statistic: -23.115
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

Impressions:
  t-statistic: -21.094
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

CTR:
  t-statistic: 10.882
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

Position:
  t-statistic: 5.041
  p-value: 0.0000
  Result: ✓ SIGNIFICANT

```


---

[← Back to Index](./00_index.md)
