import requests

url = "http://127.0.0.1:8000/translate"

data = {
    "text": "Hello, how are you?",
    "src_lang": "en",
    "dest_lang": "ta"
}

response = requests.post(url, json=data)

print(response.json())