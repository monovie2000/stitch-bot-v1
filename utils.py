# utils

import time, logging

def retry_request(fn, retries=3, delay=3):
    for attempt in range(retries):
        try:
            return fn()
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(delay)

def sanitize_input(text):
    return text.strip().replace('\n', ' ').replace('\r', '')[:300]