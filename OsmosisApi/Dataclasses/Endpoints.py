from dataclasses import dataclass
from .Enums import Chain

"""
Entry point for the Osmosis API hosted by Imperator.co

Attributes
==========
    >> chain (str): Host blockchain
    >> root (str): Main entry point for the API
    >> urls (dict): A dictionary of API endpoints

Documentation for the endpoints is found at:
https://api-osmosis.imperator.co/swagger/
"""

@dataclass
class Endpoints:
    chain: str
    root: str
    urls: dict[str, any]

    def check_status(self) -> bool:
        """Returns True if endpoints are functional"""
        health_endpoint = self.root + self.urls["health"]
        resp = requests.get(health_endpoint).json()
        return resp.get("InfluxDB") == "KO" and resp.get("PostgresSQL") == "OK"

OSMO_ENDPOINTS = {
    "health": "/health/v1/check",
    "overview": {
        "metrics": "/overview/v1/metrics",
        "message": "/overview/v1/message",
    },
    "ibc": {
        "root": "/ibc/v1/all",
        "info": "/ibc/v1/info",
        "source": "/ibc/v1/source/",
        "dest": "/ibc/v1/destination/",
        "raw": "/ibc/v1/raw",
    },
    "pairs": {
        "root": "/pairs/v1/summary",
        "historical": "/pairs/v1/historical/",
        "twap": "/pairs/v1/tawp/",
    },
    "pools": {
        "root": "/pools/v2/",
        "all": "/pools/v2/all",
        "liquidity": "/pools/v2/liquidity/",
        "volume": "/pools/v2/volume",
    },
    "tokens": {
        "root": "/tokens/v2/",
        "all": "/tokens/v2/all",
        "mcap": "/tokens/v2/mcap",
        "historical": "/tokens/v2/historical/",
        "volume": "/tokens/v2/volume/",
        "price": "/tokens/v2/price/",
        "top": "/tokens/v2/top/",
        "global_volume": "/tokens/v2/volume/global",
    },
    "liquidity": "/liquidity/v2/historical/chart",
    "volume": {
        "root": "/volume/v2/total",
        "historical_chart": "/volume/v2/historical/chart",
        "historical_global": "/volume/v2/historical/global",
    },
    "fees": {
        "total": "/fees/v1/total",
        "pools": "/fees/v1/pools",
        "root": "/fees/v1/",
        "total_historical": "/fees/v1/total/historical",
        "historical": "/fees/v1/historical/",
    },
    "apr": {
        "root": "/apr/v2/",
        "all": "/apr/v2/all",
        "staking": "/apr/v2/staking",
    },
    "supply": {
        "osmo": "/supply/v1/osmo",
        "ion": "/supply/v1/ion",
        "atom": "/supply/v1/atom",
    }
}

endpoints = Endpoints(
    chain=Chain.OSMOSIS,
    root="https://api-osmosis.imperator.co",
    urls=OSMO_ENDPOINTS
)
