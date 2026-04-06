from django.urls import path
from .views import Accommodations

urlpatterns = [
    path("", Accommodations.as_view(), name="accommodation_recommendations"),
]
