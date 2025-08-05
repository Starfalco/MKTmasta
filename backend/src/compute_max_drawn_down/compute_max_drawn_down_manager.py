import os
import pandas as pd
from json import loads
import yfinance as yf
from curl_cffi import requests
from datetime import date
from ..extracts_price.extracts_price_manager import extracts_price


class compute_max_drawn_down:

    def get_max_drawn_down(symbol: str = None, start_date: date = None, end_date: date = None):

        try:

            session = requests.Session(impersonate="chrome")

            df = yf.download(
                symbol, start=start_date, end=end_date, session=session, group_by="ticker"
            ).stack(level=0)

            df = pd.DataFrame(df.to_records())

            result = df.to_json(orient="records")
            response = loads(result)

        except Exception as e:

            response = e

        return response
    
    def build_max_drawn_down(my_df):

        MDD = 0
        data = {'MDD':'no MDD', 'Occurrence':'no occurrence', 'Max Price':'no MaxPrice'} 
        
        for index in range(1, len(my_df)):
            gap = my_df.loc[len(my_df)-1,'Adj Close']/my_df.loc[len(my_df) - index,'Adj Close'] - 1
            if gap < MDD:
                
                MDD = gap
                occurrence = my_df.loc[len(my_df)-index,'Date']
                MaxPrice = my_df.loc[len(my_df)-index,'Adj Close']
                data = {'MDD':["{:.2%}".format(MDD)], 'Occurrence':[occurrence], 'Max Price':[MaxPrice]} 
        
        output = pd.DataFrame(data, index = [0])
        
        #output = ("{:.2%}".format(MDD),occurrence)
    
        return output
    
    def get_price():
        return
