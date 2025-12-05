from django.urls import path
from .views import login_view, register_view, logout_view, check_username

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check_username'),
]
