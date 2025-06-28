import os
import pandas as pd
from json import loads


class earnings_estimate:
    path_earnings_estimate = "extracts/earnings_estimate.parquet"

    def get_earnings_estimate(symbol: str):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))

        data_path = os.path.join(parent_dir, "extracts", "earnings_estimate.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow")
        df = df[df["Ticker"] == symbol.upper()]
        result = df.to_json(orient="records")
        parsed = loads(result)

        return parsed
