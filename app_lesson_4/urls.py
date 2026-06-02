from django.urls import path
from .views import less

urlpatterns = [
    path('', less),
]