from django.urls import path
from .views import ask_meditron

urlpatterns = [
    # path("ask/", ask_meditron, name="ask_meditron"),
    path('agents/ask/', ask_meditron, name='ask_meditron'),
]
