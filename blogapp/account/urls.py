from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("signin", views.signin_request, name="signin"),
    path("logout", views.logout_request, name="logout"),
]