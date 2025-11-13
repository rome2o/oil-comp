# Period-Based Performance Comparison

## 4. Period-Based Performance Comparison

```python
# Calculate statistics by period
period_stats = gsc_dates.groupby('Period').agg({
    'Clicks': ['mean', 'median', 'std', 'sum'],
    'Impressions': ['mean', 'median', 'std', 'sum'],
    'CTR': ['mean', 'median', 'std'],
    'Position': ['mean', 'median', 'std']
}).round(2)

print("Performance Statistics by Period:\n")
print(period_stats)

# Create comparison visualization
period_summary = gsc_dates.groupby('Period')[['Clicks', 'Impressions', 'CTR', 'Position']].mean()

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('Average Performance Metrics by Period', fontsize=16, fontweight='bold')

# Clicks
period_summary['Clicks'].plot(kind='bar', ax=axes[0,0], color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
axes[0,0].set_title('Average Daily Clicks', fontsize=14, fontweight='bold')
axes[0,0].set_ylabel('Clicks')
axes[0,0].tick_params(axis='x', rotation=45)

# Impressions
period_summary['Impressions'].plot(kind='bar', ax=axes[0,1], color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
axes[0,1].set_title('Average Daily Impressions', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('Impressions')
axes[0,1].tick_params(axis='x', rotation=45)

# CTR
period_summary['CTR'].plot(kind='bar', ax=axes[1,0], color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
axes[1,0].set_title('Average CTR', fontsize=14, fontweight='bold')
axes[1,0].set_ylabel('CTR')
axes[1,0].tick_params(axis='x', rotation=45)

# Position (lower is better)
period_summary['Position'].plot(kind='bar', ax=axes[1,1], color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
axes[1,1].set_title('Average Search Position (Lower = Better)', fontsize=14, fontweight='bold')
axes[1,1].set_ylabel('Position')
axes[1,1].tick_params(axis='x', rotation=45)
axes[1,1].invert_yaxis()

plt.tight_layout()
plt.savefig('../../analysis/visualizations/period_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Period comparison visualization saved")
```

**Output:**

```
Performance Statistics by Period:

                  Clicks                      Impressions                    \
                    mean median    std    sum        mean   median      std   
Period                                                                        
Allen Post-Theme  127.95  125.0  19.42  12155    13845.68  13583.0  2077.53   
Allen Pre-Theme    68.61   69.0  27.61  10771     6836.54   5895.0  4018.10   
Previous Agency    21.26   21.0  10.60   4656      939.85    623.0   840.57   

                            CTR              Position                
                      sum  mean median   std     mean median    std  
Period                                                               
Allen Post-Theme  1315340  0.01   0.01  0.00    17.63  21.92   6.60  
Allen Pre-Theme   1073337  0.01   0.01  0.01    27.80  25.88   5.75  
Previous Agency    205828  0.05   0.03  0.05    34.13  37.61  14.95  

```

*[Chart/Visualization displayed]*

```

✓ Period comparison visualization saved

```


---

[← Back to Index](./00_index.md)
