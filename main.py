from fastapi import FastAPI, Body
from asyncio import sleep
from config import CHAT_GPT_TOKEN
from openai import AsyncOpenAI, ChatCompletion, AsyncStream
from json import loads

app = FastAPI()
client = AsyncOpenAI(api_key=CHAT_GPT_TOKEN)

@app.get("/")
async def test_work():
    return {"state": "Waiting for the thunder"}


@app.post("/ask")
async def ask_chatgpt(
    context: list[dict] = Body(embed=True),
    model: str = Body(embed=True),
    token: str = Body(embed=True)
):
    with open("keys.json", "r", encoding="utf-8") as f:
        keys = loads(f.read())
    
    if token not in keys.values():
        return {"error": "token not found"}

    completion = await client.chat.completions.create(model=model, messages=context)
    return {"result": completion}
