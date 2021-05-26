import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import forecaster # custom function

# Ticker lists (from two sources combined, because I couldn't find one good reliable list anywhere)
ticklist1 = pd.read_csv('https://github.com/shilewenuw/get_all_tickers/raw/master/get_all_tickers/tickers.csv', header = None)
ticklist2 = pd.read_csv('https://raw.githubusercontent.com/ZachDischner/Stocks/master/company_lists/NASDAQ.csv', header = None)
ticklist = np.sort(np.unique(ticklist1.append(ticklist2).values))

# Initialize forecast/figure
initial_figure = forecaster.main('AAPL')

# Build the app
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id="line-chart", figure=initial_figure),
    dcc.Dropdown(
        id='select-ticker',
        options=[{'label': i, 'value': i} for i in ticklist],
        value='AAPL')
])

@app.callback(
    Output("line-chart", 'figure'),
    [Input("select-ticker", 'value')])

def update_line_chart(ticker):
    fig = go.Figure(forecaster.main(ticker))
    return fig

app.run_server(host="0.0.0.0", port=int("8080"), debug=False)
