from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "PS04 Personalized AI Learning Agent"}
