from fastapi import FastAPI
from app.api import router as echo_router

app = FastAPI()
app.include_router(echo_router)
