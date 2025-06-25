from fastapi import APIRouter

router = APIRouter(prefix="/retrieve",
    tags=["retrieve"])

@router.get("/price/{symbol}")
async def get(symbol : str):



    return {"message : "+symbol}