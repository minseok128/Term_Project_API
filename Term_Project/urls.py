from django.urls import path, include
from .views import helloAPI, Show_extinguisher, Show_extinguisher_num

urlpatterns = [
    path("hello/", helloAPI),
    path("all/", Show_extinguisher),
    path("<int:id>/", Show_extinguisher_num),
]
