from django.urls import path, include
from .views import helloAPI, Show_extinguisher

urlpatterns = [
    path("hello/", helloAPI),
    path("all/", Show_extinguisher),
]
