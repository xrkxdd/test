from django.urls import path

from . import admin
from .views import HomeView  # Ensure this import is correct

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
