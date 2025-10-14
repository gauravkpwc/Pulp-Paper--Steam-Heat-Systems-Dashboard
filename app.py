# Heatmap with meaningful axes
sections = [f"Sec-{i+1}" for i in range(leak_severity.shape[1])]
zones = [f"Zone-{i+1}" for i in range(leak_severity.shape[0]]

heatmap_fig = px.imshow(
    leak_severity,
    x=sections,
    y=zones,
    color_continuous_scale='RdYlGn_r',
    title='Leak Detection Heatmap',
    labels={'x': 'Pipeline Sections', 'y': 'Plant Zones', 'color': 'Leak Severity'}
)

heatmap_fig.update_layout(
    xaxis=dict(title='Pipeline Sections', tickangle=45),
    yaxis=dict(title='Plant Zones'),
    margin=dict(l=40, r=40, t=60, b=40)
)

row1_col1.subheader("Leak Detection Heatmap")
row1_col1.plotly_chart(heatmap_fig, use_container_width=True)
row1_col1.caption("Visualizes leak severity across plant zones and pipeline sections for quick maintenance prioritization.")
