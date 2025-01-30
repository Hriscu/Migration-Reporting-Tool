import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GetTopicName:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError('API_KEY environment variable is not set')
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        self.headers = {"Content-Type": "application/json"}

    def get_content(self, prompt):
        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        try:
            response = requests.post(self.url, headers=self.headers, json=payload, params={"key": self.api_key}, timeout=60)
            response.raise_for_status() # Raise HTTPError for bad requests
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch content: {e}")
