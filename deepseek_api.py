# deepseek_api.py

import requests, os
from utils import retry_request

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_fashion(prompt: str, image_url: str) -> str:
    response = retry_request(
        lambda: requests.post(
            "https://api.deepseek.com/v1/fashion/estimate",
            headers=HEADERS,
            json={"prompt": prompt, "image_url": image_url},
            timeout=15
        )
    )
    return response.json()['result']