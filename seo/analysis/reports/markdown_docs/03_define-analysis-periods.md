# Define Analysis Periods

## 2. Define Analysis Periods

```python
# Define key dates
allen_start_date = pd.to_datetime('2025-02-12')
theme_change_date = pd.to_datetime('2025-07-19')
analysis_end_date = pd.to_datetime('2025-10-22')

# Add period labels to the data
def categorize_period(date):
    if date < allen_start_date:
        return 'Previous Agency'
    elif date < theme_change_date:
        return 'Allen Pre-Theme'
    else:
        return 'Allen Post-Theme'

gsc_dates['Period'] = gsc_dates['Date'].apply(categorize_period)

# Display period breakdown
print("Data Distribution by Period:")
print(gsc_dates['Period'].value_counts().sort_index())
print(f"\nTotal days analyzed: {len(gsc_dates)}")

# Calculate days in each period
for period in ['Previous Agency', 'Allen Pre-Theme', 'Allen Post-Theme']:
    period_data = gsc_dates[gsc_dates['Period'] == period]
    if len(period_data) > 0:
        print(f"\n{period}:")
        print(f"  Days: {len(period_data)}")
        print(f"  Date range: {period_data['Date'].min().date()} to {period_data['Date'].max().date()}")
```

**Output:**

```
Data Distribution by Period:
Period
Allen Post-Theme     95
Allen Pre-Theme     157
Previous Agency     219
Name: count, dtype: int64

Total days analyzed: 471

Previous Agency:
  Days: 219
  Date range: 2024-07-08 to 2025-02-11

Allen Pre-Theme:
  Days: 157
  Date range: 2025-02-12 to 2025-07-18

Allen Post-Theme:
  Days: 95
  Date range: 2025-07-19 to 2025-10-21

```


---

[← Back to Index](./00_index.md)
