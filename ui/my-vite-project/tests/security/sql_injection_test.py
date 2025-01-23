import requests

url = "http://localhost:5000/log"
payload = {
    "timestamp": "2024-12-08T12:00:00Z",
    "action": "' OR 1=1 --",
    "page": "/dashboard"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())
