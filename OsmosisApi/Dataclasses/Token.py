from dataclasses import dataclass, field
from typing import List, Dict
import pandas as pd


"""
A wrapper for storing data related to a specific cryptocurrency.

Attributes                      Description
==========                      ===========
    price (float):              Most recent price in USD
    denom (str):                A representation of the currency denominator as stored in liquidity pools
    symbol (str):               Ticker for the currency
    liquidity (float):          Total liquidity of a currency at Osmosis in USD
    volume_24h (float):         Accumulated trading volume within the last 24 hours
    volume_24h_change (float):  Net change in the trading volume within the last 24 hours
    name (str):                 Complete name of currency
    price_24h_change:           Net change of the currency price within the last 24 hours
    price_7d_chage:             Net change of the curreny price within the last 7 days
    exponent (int):             Scaling factor (volume x 10^n where n = exponent)
    display (str):              Display name for the currency

Methods
=======
    as_series: converts the Token object as a pandas Series
"""
@dataclass
class Token:
    price: float
    denom: str
    symbol: str
    liquidity: float
    volume_24h: float
    volume_24h_change: float
    name: str
    price_24h_change: float
    price_7d_change: float
    exponent: int
    display: str

    def __str__(self) -> str:
        string = (
            f"Token: {self.symbol}\n"
            f"Price: {self.price} USDT\n"
            f"Liquidity: {self.liquidity}\n"
            f"24h Volume: {self.volume_24h}"
        )
        return string

    def as_series(self) -> pd.Series:
        return pd.Series(self.__dict__)
