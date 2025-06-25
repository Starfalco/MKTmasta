from fastapi import FastAPI
from earnings_estimate.earnings_estimate_controller import earnings_estimate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/retrieve/price/{symbol}")
async def price(symbol : str):



    return {"message : "+symbol}

@app.get("/retrieve/earnings_estimate/{symbol}")
async def price(symbol : str):

    get_earnings_estimate = earnings_estimate.get_earnings_estimate(symbol)

    return get_earnings_estimate