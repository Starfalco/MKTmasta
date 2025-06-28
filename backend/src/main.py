from fastapi import FastAPI

from .earnings_estimate import earnings_estimate_controller
from .price import price_controller

app = FastAPI()


app.include_router(earnings_estimate_controller.router)
app.include_router(price_controller.router)
