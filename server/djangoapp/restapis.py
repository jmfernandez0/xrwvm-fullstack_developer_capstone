import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join(f"{k}={v}" for k, v in kwargs.items())

    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception:
        print("Network exception occurred")
        return []


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + quote(text)
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        return response.json()
    except Exception:
        print("Network exception occurred")
        return {"status": 500}
