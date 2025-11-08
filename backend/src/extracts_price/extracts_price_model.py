from typing import Optional
from pydantic import BaseModel, Field
from datetime import date as dt


class extracts_price_model(BaseModel):
    date: Optional[dt]  = Field(validation_alias="Date")
    ticker: Optional[str] = Field(validation_alias="Ticker")
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[float]
