from enum import Enum

"""
An enumeration of all valid blockchains within the Cosmos ecosystem.
"""
class Chain(Enum):
    COSMOS = "Comsos"
    EVMOS = "Evmos"
    JUNE = "Juno"
    KUJIRA = "Kujira"
    OSMOSIS = "Osmosis"
    STARGAZE = "Stargaze"

    def __str__(self) -> str:
        self.value

    def __repr__(self) -> str:
        self.value
