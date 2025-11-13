# Top Performing Queries and Pages

## 7. Top Performing Queries and Pages

```python
# Analyze top queries
print("Top 20 Performing Queries by Clicks:\n")
top_queries = gsc_queries.nlargest(20, 'Clicks')[['Top queries', 'Clicks', 'Impressions', 'CTR', 'Position']]
print(top_queries.to_string(index=False))

# Visualize top queries
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Top 15 by clicks
top_15_clicks = gsc_queries.nlargest(15, 'Clicks')
ax1.barh(range(len(top_15_clicks)), top_15_clicks['Clicks'])
ax1.set_yticks(range(len(top_15_clicks)))
ax1.set_yticklabels(top_15_clicks['Top queries'], fontsize=10)
ax1.set_xlabel('Clicks', fontsize=12)
ax1.set_title('Top 15 Queries by Clicks', fontsize=14, fontweight='bold')
ax1.invert_yaxis()

# Top 15 by impressions
top_15_impressions = gsc_queries.nlargest(15, 'Impressions')
ax2.barh(range(len(top_15_impressions)), top_15_impressions['Impressions'])
ax2.set_yticks(range(len(top_15_impressions)))
ax2.set_yticklabels(top_15_impressions['Top queries'], fontsize=10)
ax2.set_xlabel('Impressions', fontsize=12)
ax2.set_title('Top 15 Queries by Impressions', fontsize=14, fontweight='bold')
ax2.invert_yaxis()

plt.tight_layout()
plt.savefig('../../analysis/visualizations/top_queries.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Query analysis complete")
```

**Output:**

```
Top 20 Performing Queries by Clicks:

                                     Top queries  Clicks  Impressions    CTR  Position
                                            hbno    4753        21180 0.2244      1.48
                             hbno essential oils    1252         3202 0.3910      1.23
                                       hbno oils     411         1303 0.3154      1.26
                             hbno black seed oil     253         1100 0.2300      1.79
                            hbno helichrysum oil     202          641 0.3151      1.05
                 castor oil in nose side effects     174         1533 0.1135      2.25
                                 hbno rose water     137          440 0.3114      1.75
                  health and beauty natural oils     125         1228 0.1018      2.18
                             castor oil benefits     104         4470 0.0233      2.96
                    health & beauty natural oils      91          569 0.1599      1.86
                     hbno organic black seed oil      82          337 0.2433      1.79
           castor oil on feet overnight benefits      80         6287 0.0127      4.98
                               castor oil in ear      76         3614 0.0210      6.58
                              hbno essential oil      72          215 0.3349      1.27
benefits of applying castor oil on feet at night      70         1010 0.0693      2.84
                                   hbno chico ca      66          498 0.1325      2.05
                     hbno essential oils reviews      64          727 0.0880      4.98
                castor oil in nose for allergies      64          722 0.0886      3.91
                              castor oil in nose      63          827 0.0762      4.31
                              castor oil on feet      62         6344 0.0098      4.23

```

*[Chart/Visualization displayed]*

```

✓ Query analysis complete

```


---

[← Back to Index](./00_index.md)
