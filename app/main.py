from fastapi import FastAPI
from app.routers import auth

app = FastAPI()

app.include_router(auth.router, tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the User Authentication & Profile API"}
