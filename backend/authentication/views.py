from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .firebase_auth import verify_token

import firebase_admin
from firebase_admin import auth

@csrf_exempt
def authenticate_user(request):
    print("Request method:", request.method)  # Debugging line
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            uid = data.get("uid")  # ✅ Change from 'id_token' to 'uid'
            
            if not uid:
                return JsonResponse({"error": "Missing UID"}, status=400)

            # Fetch user details from Firebase using UID
            try:
                user = auth.get_user(uid)
                user_data = {
                    "uid": user.uid,
                    "email": user.email,
                    "phone_number": user.phone_number,
                    "display_name": user.display_name
                }
                return JsonResponse({"message": "Authenticated", "user": user_data})
            except auth.UserNotFoundError:
                return JsonResponse({"error": "User not found"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)




# Ensure Firebase is initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app()

@csrf_exempt
def signup_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"error": "Email and Password are required"}, status=400)

            # Create user in Firebase Authentication
            user = auth.create_user(email=email, password=password)

            return JsonResponse({"message": "User created successfully", "uid": user.uid}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=400)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")
            
            if not email or not password:
                return JsonResponse({"error": "Email and password required"}, status=400)

            # Authenticate with Firebase
            user = auth.get_user_by_email(email)
            return JsonResponse({"message": "Authenticated", "user": {"uid": user.uid, "email": user.email}})
        
        except auth.UserNotFoundError:
            return JsonResponse({"error": "Invalid email or password"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)