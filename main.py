from fastapi import FastAPI
import uvicorn
from app.routers import pokeberries_stats, pokeberries_html
from dotenv import load_dotenv
import os

load_dotenv()
enviroment = os.getenv("ENVIRONMENT")

app = FastAPI(
    title="Pokeberries statistics API",
    description=f"This is a simple API that returns statistics about the Pokeberries API. This is the {enviroment} enviroment.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(pokeberries_stats.router)
app.include_router(pokeberries_html.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, workers=4)