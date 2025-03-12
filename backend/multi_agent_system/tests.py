import requests

django_api_url = "http://127.0.0.1:8000/agents/ask/"
response = requests.get(django_api_url, params={"query": "Medicine for Fever"})
print(response.json())
