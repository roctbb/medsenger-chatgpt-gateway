from fastapi import FastAPI
from asyncio import sleep

app = FastAPI()


@app.get("/")
async def root():
    print("get")
    await sleep(20)
    return {"state": "Waiting for the thunder"}


@app.get("/h")
async def say_hello():
    return {"message":"Hello "}
