from typing import Optional
from pydantic import BaseModel, Field
from datetime import date as dt


class retrieve_price_model(BaseModel):
    date: Optional[dt] = Field(validation_alias="Date")
    ticker: Optional[str] = Field(validation_alias="Ticker")
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    adjClose: Optional[float] = None
