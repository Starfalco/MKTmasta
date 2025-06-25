from fastapi import APIRouter
from backend.src.earnings_estimate.earnings_estimate_manager import earnings_estimate

router = APIRouter(prefix="/retrieve",
    tags=["retrieve"])

@router.get("/earnings_estimate/{symbol}")
async def get(symbol : str):

    get_earnings_estimate = earnings_estimate.get_earnings_estimate(symbol)

    return get_earnings_estimate