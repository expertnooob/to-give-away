from django.urls import path
from .views import UserRegistrationView, UserLoginView, PasswordResetView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
