import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Simulated data
np.random.seed(42)
time_series = pd.date_range(start='2023-01-01', periods=100, freq='D')
boiler_efficiency = np.random.normal(loc=87, scale=2, size=100)
stack_temp = np.random.normal(loc=250, scale=20, size=100)
o2_levels = np.random.normal(loc=5, scale=1, size=100)
leak_severity = np.random.rand(10, 10)  # Heatmap data
condensate_recovery = 92
steam_per_kg_paper = 1.2
leak_loss_percent = -2.5  # Simulating negative KPI for demo

# Dashboard Title
st.title("Steam & Heat Systems Dashboard")

# KPIs Row
st.markdown("### Key KPIs")
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<div style='font-size:18px; font-weight:bold;'>Steam/kg of paper:<br>{steam_per_kg_paper:.2f} kg</div>", unsafe_allow_html=True)
col2.markdown(f"<div style='font-size:18px; font-weight:bold;'>Boiler Efficiency:<br>{np.mean(boiler_efficiency):.2f}%</div>", unsafe_allow_html=True)
col3.markdown(f"<div style='font-size:18px; font-weight:bold;'>Condensate Return:<br>{condensate_recovery:.2f}%</div>", unsafe_allow_html=True)

color = "red" if leak_loss_percent < 0 else "black"
col4.markdown(f"<div style='font-size:18px; font-weight:bold; color:{color};'>Leak Loss %:<br>{leak_loss_percent:.2f}%</div>", unsafe_allow_html=True)

# Charts in 2x2 Grid
st.markdown("### System Visualizations")
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# Heatmap with meaningful axes and dynamic height
sections = [f"Sec-{i+1}" for i in range(leak_severity.shape[1])]
zones = [f"Zone-{i+1}" for i in range(leak_severity.shape[0])]
heatmap_height = 50 * leak_severity.shape[0]  # Dynamic height

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
    height=heatmap_height,
    margin=dict(l=40, r=40, t=60, b=40)
)
row1_col1.subheader("Leak Detection Heatmap")
row1_col1.plotly_chart(heatmap_fig, use_container_width=True)
row1_col1.caption("Visualizes leak severity across plant zones and pipeline sections for quick maintenance prioritization.")

# Boiler Efficiency Trend
efficiency_fig = go.Figure()
efficiency_fig.add_trace(go.Scatter(x=time_series, y=boiler_efficiency,
                                    mode='lines', name='Efficiency (%)'))
efficiency_fig.update_layout(title='Boiler Efficiency Trend',
                             xaxis_title='Date', yaxis_title='Efficiency (%)')
row1_col2.subheader("Boiler Efficiency Trend")
row1_col2.plotly_chart(efficiency_fig, use_container_width=True)
row1_col2.caption("Tracks boiler performance over time to ensure optimal fuel usage and cost control.")

# Condensate Recovery Gauge
gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=condensate_recovery,
    delta={'reference': 90, 'increasing': {'color': "green"}},
    gauge={'axis': {'range': [0, 100]},
           'bar': {'color': "blue"},
           'steps': [
               {'range': [0, 90], 'color': "lightgray"},
               {'range': [90, 100], 'color': "lightgreen"}],
           'threshold': {'line': {'color': "red", 'width': 4},
                         'thickness': 0.75, 'value': 90}},
    title={'text': "Condensate Recovery (%)"}
))
row2_col1.subheader("Condensate Recovery Gauge")
row2_col1.plotly_chart(gauge_fig, use_container_width=True)
row2_col1.caption("Shows recovery efficiency; higher recovery reduces water and energy costs.")

# Scatter Plot
scatter_fig = px.scatter(x=stack_temp, y=o2_levels,
                         labels={'x': 'Stack Temperature (°C)', 'y': 'O₂ Levels (%)'},
                         title='Stack Temperature vs O₂ Levels')
row2_col2.subheader("Stack Temperature vs O₂ Levels")
row2_col2.plotly_chart(scatter_fig, use_container_width=True)
row2_col2.caption("Correlates temperature and oxygen levels to optimize combustion efficiency.")
