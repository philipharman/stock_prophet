import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

def main(TICK):
    # Get stock data + organize
    stock = yf.Ticker(TICK)
    hist = pd.DataFrame(stock.history(period='3y'))
    hist.index = pd.to_datetime(hist.index)
    hist.dropna(inplace=True)
    pseries = pd.DataFrame()
    pseries['ds'] = hist.index
    pseries['y'] = hist.Close.values

    # Prophet prediction
    model = Prophet()
    model.fit(pseries)
    future = model.make_future_dataframe(periods=180)
    forecast = model.predict(future)

    # Make plot
    figure = plot_plotly(model, forecast)
    figure.update_layout(
        title = '6-Month Projection: {}'.format(TICK),
        xaxis_title="Date",
        yaxis_title="Closing Value",
        font=dict(family="Courier New, monospace",size=18))

    return figure
