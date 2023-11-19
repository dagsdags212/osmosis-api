from requests import get
from pandas import DataFrame

def list_tokens(sort_by: str = "volume_24h") -> DataFrame:
    endpoint = ENDPOINTS["tokens"]["all"]
    resp = get(ROOT+endpoint)
    token_df = DataFrame([Token(**data).as_series() for data in resp.json()])
    cols = ["symbol", "name", "price", "volume_24h", "liquidity"]
    if sort_by in token_df.columns:
        token_df = token_df.sort_values(by=sort_by, ascending=False)
    else:
        raise ValueError(f"`sort_by` arugment must be one of the following: {list(token_df.columns)}")
    return token_df[cols]
