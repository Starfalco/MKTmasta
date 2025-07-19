import os
import pandas as pd
from json import loads
import yfinance as yf
from curl_cffi import requests
from datetime import date


class extracts_earnings_dates:


    def get_earnings_dates(symbol: str = None):

        try:

            session = requests.Session(impersonate="chrome")

            df = pd.DataFrame(yf.Ticker("aapl", session=None).get_earnings_dates()).reset_index()

            df = pd.DataFrame(df.to_records())

            result = df.to_json(orient="records")
            response = loads(result)

        except Exception as e:

            response = e

        return response
