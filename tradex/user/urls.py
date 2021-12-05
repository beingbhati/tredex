from django.urls import path
from user import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]