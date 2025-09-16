from django.urls import path
from .views import RegisterView, LoginView, AdminView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin-view/', AdminView.as_view(), name='admin-view'),
]