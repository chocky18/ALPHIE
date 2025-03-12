import requests

django_api_url = "http://127.0.0.1:8000/agents/ask/"
response = requests.get(django_api_url, params={"query": "medication for cold and fever for adults?"})
print(response.json())
