import json
from typing import Tuple

import requests

from config import BASE_URL


def api_get_access_token(verify_token: str, phone_number: str) -> Tuple[str, str]:
    url = BASE_URL + f"/phone/v1/Verification/verify?verifyToken={verify_token}"

    payload = json.dumps({
        "phoneNumber": phone_number
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.post(url=url, headers=headers, data=payload)

    if response.status_code != 202:
        raise AssertionError(f"Status code for {url} is {response.status_code}")
    else:
        return response.json().get("access_token"),  response.json().get("refresh_token")
