from django.urls import path
from .views import hello_world_app_view

urlpatterns = [
    path('helloworldapp/', hello_world_app_view),
]
