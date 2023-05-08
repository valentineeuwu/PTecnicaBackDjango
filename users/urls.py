from django.urls import path
from .views import RegisterUserView, login, get_user_data, revoke_token

urlpatterns = [
    path('login', login),
    path('register', RegisterUserView.as_view(), name="register"),
    path('user', get_user_data, name="current_user"),
    path('logout', revoke_token),
]

