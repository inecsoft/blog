from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"), 
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("oauth/", include("social_django.urls"), name="oauth"),    
    
]