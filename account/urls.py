from django.urls import path
from .views import LoginView, LogoutView, register


app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]

