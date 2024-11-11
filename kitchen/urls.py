from django.urls import path
from .views import HomeView  # Ensure this import is correct

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
