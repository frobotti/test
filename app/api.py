from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/echo")
async def echo(request: Request):
    body = await request.json()
    msg = body.get("message", "No message provided")
    return {"echo": "you said: " + msg}
