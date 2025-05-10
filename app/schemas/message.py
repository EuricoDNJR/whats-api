from pydantic import BaseModel


class MessagePayload(BaseModel):
    to: str
    text: str
