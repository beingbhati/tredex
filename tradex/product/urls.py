from django.urls import path
from product import views

urlpatterns = [
    path("something", views.something, name="something"),
]