# imgbb.py

import requests, os
from utils import retry_request

IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

def upload_image_to_imgbb(image_bytes):
    response = retry_request(
        lambda: requests.post(
            "https://api.imgbb.com/1/upload",
            data={"key": IMGBB_API_KEY},
            files={"image": image_bytes},
            timeout=10
        )
    )
    return response.json()['data']['url']