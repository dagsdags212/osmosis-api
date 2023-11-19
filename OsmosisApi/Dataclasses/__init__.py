from dataclasses import dataclass
from datetime import datetime
import requests
from pandas import DataFrame

from .Endpoints import endpoints as OSMO_ENDPOINTS
from .Enums import Chain
from .Token import Token

class Overview:
    volume_24h: float
    volume_24h_change: float
    liquidity_usd: float
    liquidity_usd_24h: float
    dt: datetime = datetime.now()

    def __init__(self) -> None:
        metrics_endpoint = OSMO_ENDPOINTS.root + OSMO_ENDPOINTS.urls["overview"]["metrics"]
        resp = requests.get(metrics_endpoint).json()
        self.volume_24h = resp.get("volume_24h")
        self.volume_24h_change = resp.get("volume_24h_change")
        self.liquidity_usd = resp.get("liquidity_usd")
        self.liquidity_usd_24h = resp.get("liquidity_usd_24h")

    def tabulate(self) -> DataFrame:
        index = list(self.__dict__.keys())
        data = list(self.__dict__.values())
        return DataFrame(data={"data": data}, index=index)
