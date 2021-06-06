from django.urls import path
from . import views

from accounts.views import (
    AccountRegistration, AccountRegistrationSuccess,
    AccountLogin, AccountLogout, list, profile, follow, recommendations)

app_name = "accounts"
urlpatterns = [
    path("accounts/list/", list, name="list"),
    path("accounts/register/", AccountRegistration.as_view(), name="register"),
    path("accounts/register-success/", AccountRegistrationSuccess.as_view(), name="register-success"),
    path("accounts/login/", AccountLogin.as_view(), name="login"),
    path("accounts/logout/", AccountLogout.as_view(), name="logout"),
    path("profile/<str:username>/", profile, name="profile"),
    path("follow/<str:username>/", follow, name="follow"),
    path("recommendations/", recommendations, name="recommendations"),
]
