from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class extracts_price_model(BaseModel):
    Date: Optional[date] = None
    Ticker: Optional[str] = None
    Open: Optional[float] = None
    High: Optional[float] = None
    Low: Optional[float] = None
    Close: Optional[float] = None
    Volume: Optional[float] = None
