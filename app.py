# Heatmap with meaningful axes and dynamic height
sections = [f"Sec-{i+1}" for i in range(leak_severity.shape[1])]
zones = [f"Zone-{i+1}" for i in range(leak_severity.shape[0])]

heatmap_height = 50 * leak_severity.shape[0]  # 50px per row for better readability

heatmap_fig = px.imshow(
    leak_severity,
    x=sections,
    y=zones,
    color_continuous_scale='RdYlGn_r',
    labels={'x': 'Pipeline Sections', 'y': 'Plant Zones', 'color': 'Leak Severity'}
)

heatmap_fig.update_layout(
    title='Leak Detection Heatmap',
    xaxis=dict(title='Pipeline Sections', tickangle=45),
    yaxis=dict(title='Plant Zones'),
    height=heatmap_height,  # ✅ Dynamic height based on rows
    margin=dict(l=40, r=40, t=60, b=40)
)

row1_col1.subheader("Leak Detection Heatmap")
row1_col1.plotly_chart(heatmap_fig, use_container_width=True)
row1_col1.caption("Visualizes leak severity across plant zones and pipeline sections for quick maintenance prioritization.")
