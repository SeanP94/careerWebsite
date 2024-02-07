from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="HomePage"),
    path("resume/", views.resumePage, name="Resume")
]