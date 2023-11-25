from fastapi import FastAPI, status, HTTPException
import uvicorn
from app.routers import pokeberries_stats, pokeberries_html

app = FastAPI(
    title="Pokeberries statistics API",
    description="This is a simple API that returns statistics about the Pokeberries API",
    version="1.0.0",
)

@app.get("/", status_code=status.HTTP_200_OK, tags=["Root"])
def root():
    return {"Welcome to Pokeberries statistics API!"}

app.include_router(pokeberries_stats.router)
app.include_router(pokeberries_html.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=2013, reload=True, workers=4)