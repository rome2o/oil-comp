# Data Loading

## 1. Data Loading

```python
# Load processed data
print("Loading processed datasets...\n")

# Google Search Console Time Series (PRIMARY DATA)
gsc_dates = pd.read_csv('../../analysis/processed_data/gsc_dates_timeseries.csv')
gsc_dates['Date'] = pd.to_datetime(gsc_dates['Date'])
gsc_dates = gsc_dates.sort_values('Date')
print(f"✓ GSC Time Series: {len(gsc_dates)} days")
print(f"  Date range: {gsc_dates['Date'].min()} to {gsc_dates['Date'].max()}\n")

# GSC Queries
gsc_queries = pd.read_csv('../../analysis/processed_data/gsc_queries.csv')
print(f"✓ GSC Queries: {len(gsc_queries)} queries\n")

# GSC Pages
gsc_pages = pd.read_csv('../../analysis/processed_data/gsc_pages.csv')
print(f"✓ GSC Pages: {len(gsc_pages)} pages\n")

# Core Web Vitals
cwv = pd.read_csv('../../analysis/processed_data/core_web_vitals.csv')
print(f"✓ Core Web Vitals: {len(cwv)} records\n")

# Display GSC time series summary
print("\nGSC Time Series Summary:")
print(gsc_dates.describe())
```

**Output:**

```
Loading processed datasets...

✓ GSC Time Series: 471 days
  Date range: 2024-07-08 00:00:00 to 2025-10-21 00:00:00

✓ GSC Queries: 1000 queries

✓ GSC Pages: 1000 pages

✓ Core Web Vitals: 1 records


GSC Time Series Summary:
                                Date      Clicks   Impressions         CTR  \
count                            471  471.000000    471.000000  471.000000   
mean   2025-02-28 00:00:00.000000256   58.560510   5508.503185    0.031331   
min              2024-07-08 00:00:00    1.000000     75.000000    0.001600   
25%              2024-11-02 12:00:00   21.000000    994.500000    0.009100   
50%              2025-02-28 00:00:00   38.000000   2718.000000    0.012700   
75%              2025-06-25 12:00:00   92.500000  11344.500000    0.028200   
max              2025-10-21 00:00:00  177.000000  18893.000000    0.212700   
std                              NaN   45.120124   5560.056695    0.040019   

         Position  
count  471.000000  
mean    28.689958  
min      6.120000  
25%     21.965000  
50%     25.600000  
75%     38.650000  
max     64.960000  
std     12.730830  

```


---

[← Back to Index](./00_index.md)
