from django.urls import path
from .views import HomeView  # Ensure this import is correct

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
]
