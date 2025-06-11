from .views import ShowForm
from django.urls import path

urlpatterns = [
    path('', ShowForm),
]
