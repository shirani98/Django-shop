from django.urls import path
from .views import Login, Register,ResetPass,ResetPassDone,RestPassConfirm,RestPassComplate
from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [
    path("login/", Login.as_view(),name="login" ),
    path("register/", Register.as_view(),name="register" ),
    path("logout/", LogoutView.as_view(),name="logout" ),
    path('reset/', ResetPass.as_view(),name = 'reset'),
    path('resetdone/', ResetPassDone.as_view(),name = 'resetdone'),
    path('resetdoneconfirm/<uidb64>/<token>', RestPassConfirm.as_view(),name = 'resetdoneconfirm'),
    path('resetdonecomplete/', RestPassComplate.as_view(),name = 'resetdonecomplete'),  

    
]