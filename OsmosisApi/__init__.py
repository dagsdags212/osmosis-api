from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from .helpers import *
from .Dataclasses import *


def _fetch_graphing_data(ticker: str, interval: int = 1440):
    """
    Retrieves historical price data of a currency for graphing candlestick charts.

    Parameters
    ==========
    ticker (str):   Short-hand symbol for currency.
    interval (int): Time interval in minutes. Valid values include 5, 15, 30, 60, 120, 240,
                    720, 1440, 10080, and 43800.

    Return
    ======
    A dictionary containing historical candlestick data of a currency.

    """
    assert interval in [5, 15, 30, 60, 120, 240, 720, 1440, 10080, 43800], "Invalid interval"
    endpoint = OSMO_ENDPOINTS.root + OSMO_ENDPOINTS.urls["tokens"]["historical"] + ticker + "/chart"
    payload = {"tf": interval}
    resp = get(endpoint, params=payload)
    resp.raise_for_status()
    data = resp.json()

    df_data = {
        "time": [datetime.fromtimestamp(d["time"]).date() for d in data],
        "open": [d["open"] for d in data],
        "high": [d["high"] for d in data],
        "low": [d["low"] for d in data],
        "close": [d["close"] for d in data],
    }

    df_data["direction"] = "increasing" if df_data["open"] < df_data["close"] else "decreasing"
    return pd.DataFrame(data=df_data)


def fetch_graph(ticker: str, interval: int = 1440):
    """
    Plots the historical candlestick data of a specified currency.
    Refer to `_fetch_graphing_data` for parameter details.
    """
    df = _fetch_graphing_data(ticker, interval)
    fig = go.Figure(data=[
            go.Candlestick(x=df["time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"])
        ])
    fig.update_layout(
        title=f"{ticker.upper()} Chart",
        yaxis_title=f"{ticker.upper()} Price (USDT)"
    )
    return fig
