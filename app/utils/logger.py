import logging
from datetime import datetime
import os
from typing import Union

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=f"logs/messages_{datetime.now().date()}.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def log_message(
    method: str, endpoint: str, request_body: dict, response_body: Union[dict, str]
):
    logging.info(
        f"METHOD: {method} | ENDPOINT: {endpoint}\nREQUEST: {request_body}\nRESPONSE: {response_body}\n{'-'*60}"
    )
