from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/retrieve/price/{symbol}")
async def price(symbol : str):



    return {"message : "+symbol}