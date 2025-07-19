from typing import Optional
from pydantic import BaseModel
from datetime import date


class extracts_earnings_dates_model(BaseModel):
    earningDates: Optional[date] = None
    epsEstimate: Optional[float] = None
    reportedEPS: Optional[float] = None
    suprise: Optional[float] = None
    eventType: Optional[str] = None
    Ticker: Optional[str] = None