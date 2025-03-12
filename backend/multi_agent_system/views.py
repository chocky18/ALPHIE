import requests
from django.http import JsonResponse

FASTAPI_URL = ""  # Replace with your actual ngrok URL

def ask_meditron(request):
    user_query = request.GET.get("query", "")

    if not user_query:
        return JsonResponse({"error": "No query provided"}, status=400)

    try:
        response = requests.post(f"{FASTAPI_URL}/query", json={"query": user_query}, verify=False)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({"error": "Failed to get response from FastAPI"}, status=500)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=500)
