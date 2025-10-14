import dash
from dash import dcc, html
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
leak_severity = np.random.rand(10, 10)
condensate_recovery = 92
steam_per_kg_paper = 1.2
leak_loss_percent = 3.5

# Figures
heatmap_fig = px.imshow(leak_severity, color_continuous_scale='RdYlGn_r',
                        title='Real-time Leak Detection Map')

efficiency_fig = go.Figure()
efficiency_fig.add_trace(go.Scatter(x=time_series, y=boiler_efficiency,
                                    mode='lines', name='Efficiency (%)'))
efficiency_fig.update_layout(title='Boiler Efficiency Trend',
                             xaxis_title='Date', yaxis_title='Efficiency (%)')

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

scatter_fig = px.scatter(x=stack_temp, y=o2_levels,
                         labels={'x': 'Stack Temperature (°C)', 'y': 'O₂ Levels (%)'},
                         title='Stack Temperature vs O₂ Levels')

# Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Steam & Heat Systems Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.H3("Key KPIs"),
        html.Ul([
            html.Li(f"Steam/kg of paper: {steam_per_kg_paper:.2f} kg"),
            html.Li(f"Boiler efficiency: {np.mean(boiler_efficiency):.2f}% (Target > 85%)"),
            html.Li(f"Condensate return rate: {condensate_recovery:.2f}% (Target > 90%)"),
            html.Li(f"Leak loss %: {leak_loss_percent:.2f}%")
        ])
    ], style={'marginBottom': '30px'}),

    html.Div([
        dcc.Graph(figure=heatmap_fig),
        dcc.Graph(figure=efficiency_fig),
        dcc.Graph(figure=gauge_fig),
        dcc.Graph(figure=scatter_fig)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)  # ✅ Updated method
