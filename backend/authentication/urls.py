from django.urls import path
from .views import authenticate_user
from .views import signup_user,login_user
urlpatterns = [
    path('login/', login_user, name='login'),
    path("signup/", signup_user, name="signup"),
]
