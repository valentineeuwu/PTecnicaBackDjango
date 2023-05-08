from django.urls import path
from .views import handle_click, get_sessions

urlpatterns = [
    path('click/<button>', handle_click),
    path('info', get_sessions),
]

