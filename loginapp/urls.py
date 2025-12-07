from django.urls import path
<<<<<<< HEAD
from .views import (
    login_view, register_view, logout_view, check_username,
    password_reset_request, password_reset_verify, password_reset_done
)
=======
from .views import login_view, register_view, logout_view, check_username
>>>>>>> e2f363d1db38133cafa260c091eb4d546218ad97

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check_username'),
<<<<<<< HEAD

    # OTP-based password reset
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/verify/', password_reset_verify, name='password_reset_verify'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
=======
>>>>>>> e2f363d1db38133cafa260c091eb4d546218ad97
]
