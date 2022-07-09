from django.urls import path

from accounts.views import LoginFormView, RegisterFormView, logout

urlpatterns = [
    path("register/", RegisterFormView.as_view(), name="register"),
    path("login/", LoginFormView.as_view(), name="login"),
    path("logout/", logout, name="logout")
]
