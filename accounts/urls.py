from django.urls import path
from .views import Login, Register
from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [
    path("login/", Login.as_view(),name="login" ),
    path("register/", Register.as_view(),name="register" ),
    path("logout/", LogoutView.as_view(),name="logout" ),


    
]