
from __future__ import annotations
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()
@app.get("/healthz", response_class=PlainTextResponse)
async def healthz()->str: return "ok"
