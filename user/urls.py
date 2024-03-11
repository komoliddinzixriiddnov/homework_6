from django.urls import path
from .views import  UserLoginPaggeView, UseRegisterPaggeView

urlpatterns = [
    path("login/", UserLoginPaggeView.as_view(), name="login-page"),
    path("register/", UseRegisterPaggeView.as_view(), name="register-page"),

]