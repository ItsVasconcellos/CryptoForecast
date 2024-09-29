from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.mongodb import MongoDB

from dotenv import dotenv_values

app = FastAPI()

config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI", "mongodb://db:27017")
DATABASE_NAME = config.get("DATABASE_NAME", "cryptoForecast")


@app.get("/")
async def root():
    return {"message": "Hello World"}
