from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.mongodb import MongoDB


from app.routers import log_router
from app.repositories.log_repo import LogRepository
from app.services.log_service import LogServiceSingleton, setup_logging

from dotenv import dotenv_values


config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI", "mongodb://db:27017")
DATABASE_NAME = config.get("DATABASE_NAME", "cryptoForecast")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    app.state.db = MongoDB(DATABASE_URI, DATABASE_NAME)

    log_repo = LogRepository(app.state.db)
    LogServiceSingleton.initialize(log_repo)
    logger = setup_logging(LogServiceSingleton.get_instance())

    print("Connected to the MongoDB database!")

    yield

    app.state.db.close()
    print("Disconnected to the MongoDB database!")


app = FastAPI(lifespan=app_lifespan)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(log_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
