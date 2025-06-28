from fastapi import APIRouter
from backend.src.earnings_estimate.earnings_estimate_manager import earnings_estimate
from .earnings_estimate_model import earnings_estimate_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/earnings_estimate/{symbol}")
async def get(symbol: str) -> list[earnings_estimate_model]:

    get_earnings_estimate = earnings_estimate.get_earnings_estimate(symbol)

    return get_earnings_estimate
