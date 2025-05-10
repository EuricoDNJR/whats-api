from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import PlainTextResponse
import requests

from app.schemas.message import MessagePayload
from app.utils.logger import log_message
from app.core.settings import settings

router = APIRouter()


@router.post("/send-message")
def send_message(payload: MessagePayload):
    """
    Envia uma mensagem para um número via WhatsApp Cloud API.[
    E.g:

        {
            "to": "5511999999999",
            "text": "Hello, World!"
        }

    """
    url = f"https://graph.facebook.com/v22.0/{settings.PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": payload.to,
        "type": "text",
        "text": {"body": payload.text},
    }

    response = requests.post(url, json=data, headers=headers)
    log_message("POST", "/send-message", data, response.json())

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()


@router.get("/webhook", include_in_schema=False)
def verify_webhook(request: Request):
    args = dict(request.query_params)

    mode = args.get("hub.mode")
    token = args.get("hub.verify_token")
    challenge = args.get("hub.challenge")

    if mode == "subscribe" and token == settings.VERIFY_TOKEN:
        return PlainTextResponse(content=challenge, status_code=200)

    raise HTTPException(status_code=403, detail="Invalid verification token")


@router.post("/webhook", include_in_schema=False)
async def receive_message(request: Request):
    data = await request.json()
    log_message("POST", "/webhook", data, "received")
    return {"status": "received"}
