from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome to Pokeberries statistics API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=2013, reload=True, workers=4)