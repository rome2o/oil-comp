# Time Series Visualization - Overall Trends

## 3. Time Series Visualization - Overall Trends

```python
# Create comprehensive time series plot
fig = make_subplots(
    rows=4, cols=1,
    subplot_titles=('Daily Clicks', 'Daily Impressions', 'Click-Through Rate (CTR)', 'Average Position'),
    vertical_spacing=0.08,
    specs=[[{"secondary_y": False}],
           [{"secondary_y": False}],
           [{"secondary_y": False}],
           [{"secondary_y": False}]]
)

# Add traces for each metric
fig.add_trace(
    go.Scatter(x=gsc_dates['Date'], y=gsc_dates['Clicks'], 
               name='Clicks', line=dict(color='#1f77b4', width=2)),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=gsc_dates['Date'], y=gsc_dates['Impressions'], 
               name='Impressions', line=dict(color='#ff7f0e', width=2)),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=gsc_dates['Date'], y=gsc_dates['CTR'], 
               name='CTR', line=dict(color='#2ca02c', width=2)),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(x=gsc_dates['Date'], y=gsc_dates['Position'], 
               name='Position', line=dict(color='#d62728', width=2)),
    row=4, col=1
)

# Add vertical lines for key dates
for i in range(1, 5):
    # Allen start date
    fig.add_vline(x=allen_start_date.timestamp() * 1000, 
                  line_dash="dash", line_color="green", 
                  annotation_text="Allen Starts", row=i, col=1)
    
    # Theme change date
    fig.add_vline(x=theme_change_date.timestamp() * 1000, 
                  line_dash="dash", line_color="red", 
                  annotation_text="Theme Change", row=i, col=1)

# Update layout
fig.update_layout(
    height=1200,
    title_text="SEO Performance Time Series Analysis<br><sub>Key Events: Allen Start (Feb 12) | Theme Change (Jul 19)</sub>",
    showlegend=False,
    hovermode='x unified'
)

# Update y-axes labels
fig.update_yaxes(title_text="Clicks", row=1, col=1)
fig.update_yaxes(title_text="Impressions", row=2, col=1)
fig.update_yaxes(title_text="CTR", row=3, col=1)
fig.update_yaxes(title_text="Position (lower is better)", row=4, col=1)

fig.show()

print("✓ Time series visualization complete")
```

**Output:**

*[Chart/Visualization displayed]*

```
✓ Time series visualization complete

```


---

[← Back to Index](./00_index.md)
