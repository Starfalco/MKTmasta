from fastapi import APIRouter
from .compute_max_drawn_down_manager import compute_max_drawn_down
from .compute_max_drawn_down_model import compute_max_drawn_down_model
from datetime import date

router = APIRouter(prefix="/compute", tags=["compute"])


@router.get("/compute_max_drawn_down/{symbol}")
async def get(
    symbol: str, start_date: date = None, end_date: date = None
) -> list[compute_max_drawn_down_model]:

    response = compute_max_drawn_down.get_price(symbol, start_date, end_date)

    return response
