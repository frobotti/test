from fastapi import FastAPI
from app.api import router as echo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(echo_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir esto más adelante
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)