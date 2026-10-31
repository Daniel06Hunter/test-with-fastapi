from fastapi import FastAPI

app = FastAPI(title="Bank API")

@app.get("/")
async def root():
    return {"status": "ok"}