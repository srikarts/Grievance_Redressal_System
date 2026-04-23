from django.urls import path
from .views import (
    login_view, register_view, logout_view, check_username, check_email, send_registration_otp,
    password_reset_request, password_reset_verify, password_reset_done
)

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check_username'),
    path('check-email/', check_email, name='check_email'),
    path('send-registration-otp/', send_registration_otp, name='send_registration_otp'),

    # OTP-based password reset
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/verify/', password_reset_verify, name='password_reset_verify'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
]
