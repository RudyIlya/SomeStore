from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
app_name = "accounts"

urlpatterns = [
    path("login", signup_login_view.as_view(), name="signup-login"),
    path("logout", logoutuser, name="logout"),
    path("userlogin", login_user, name="login-user"),
    path("userregister", register_user, name="register-user"),
    path("profile", profile_view.as_view(), name="profile"),
    path("updateprofile", update_profile, name="update-profile"),
    path("updateavatar", update_avatar, name="update-avatar"),

]