import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Simulated data
np.random.seed(42)
time_series = pd.date_range(start='2023-01-01', periods=100, freq='D')
boiler_efficiency = np.random.normal(loc=87, scale=2, size=100)
stack_temp = np.random.normal(loc=250, scale=20, size=100)
o2_levels = np.random.normal(loc=5, scale=1, size=100)
leak_severity = np.random.rand(10, 10)  # Heatmap data
condensate_recovery = 92  # %
steam_per_kg_paper = 1.2  # kg
leak_loss_percent = 3.5  # %

# 1. Real-time Leak Detection Map
heatmap_fig = px.imshow(leak_severity, color_continuous_scale='RdYlGn_r',
                        title='Real-time Leak Detection Map')
heatmap_fig.show()

# 2. Boiler Efficiency Trend
efficiency_fig = go.Figure()
efficiency_fig.add_trace(go.Scatter(x=time_series, y=boiler_efficiency,
                                    mode='lines', name='Efficiency (%)'))
efficiency_fig.update_layout(title='Boiler Efficiency Trend',
                             xaxis_title='Date', yaxis_title='Efficiency (%)')
efficiency_fig.show()

# 3. Condensate Recovery Gauge
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
gauge_fig.show()

# 4. Stack Temperature vs O₂ Levels
scatter_fig = px.scatter(x=stack_temp, y=o2_levels,
                         labels={'x': 'Stack Temperature (°C)', 'y': 'O₂ Levels (%)'},
                         title='Stack Temperature vs O₂ Levels')
scatter_fig.show()

# Print KPIs
print("Steam/kg of paper: {:.2f} kg".format(steam_per_kg_paper))
print("Boiler efficiency: {:.2f}% (Target > 85%)".format(np.mean(boiler_efficiency)))
print("Condensate return rate: {:.2f}% (Target > 90%)".format(condensate_recovery))
print("Leak loss %: {:.2f}%".format(leak_loss_percent))
