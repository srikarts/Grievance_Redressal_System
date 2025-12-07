from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
<<<<<<< HEAD
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import random
=======
>>>>>>> e2f363d1db38133cafa260c091eb4d546218ad97

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'loginapp/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            request.session.set_expiry(900)  # 15 mins

            # ---- Role-based LOGIN Routing ----
            if user.is_superuser:
                return redirect('cms:admin_dashboard')

            elif hasattr(user, 'profile') and user.profile.role == 'employee':
                return redirect('cms:employee_dashboard')

            else:
                return redirect('cms:user_dashboard')

        # Invalid credentials
        messages.error(request, 'Invalid username or password')
        return redirect('login')

    return render(request, 'loginapp/login.html')



@login_required
def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')

from django.http import JsonResponse

def check_username(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        from django.contrib.auth.models import User
        available = not User.objects.filter(username=username).exists()
        return JsonResponse({'available': available})
    return JsonResponse({'available': False})

<<<<<<< HEAD

def _store_otp_in_session(request, email, otp, minutes=10):
    expires_at = (timezone.now() + timedelta(minutes=minutes)).timestamp()
    request.session['password_reset_otp'] = {
        'email': email,
        'otp': otp,
        'expires_at': expires_at
    }
    request.session.modified = True

def _clear_otp_session(request):
    request.session.pop('password_reset_otp', None)
    request.session.modified = True

def password_reset_request(request):
    """
    Show email form and send OTP to the email (if user exists).
    Behaviour: do not reveal whether the email exists.
    """
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        # Generate OTP regardless; send only if user with email exists.
        otp = f"{random.randint(100000, 999999)}"
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            user = None

        # Store OTP tied to the provided email in session (so same browser can verify)
        _store_otp_in_session(request, email, otp, minutes=10)

        # Send OTP email if user exists - otherwise silently succeed
        if user:
            subject = "Your password reset OTP"
            message = f"Your OTP to reset your password is: {otp}\nThis OTP will expire in 10 minutes."
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            except Exception:
                # don't leak send failures to user; log in real app.
                pass

        messages.success(request, "If that email exists in our system, an OTP has been sent. Check your inbox.")
        return redirect('password_reset_verify')

    return render(request, 'loginapp/password_reset_form.html', {})


def password_reset_verify(request):
    """
    Verify OTP and set new password.
    """
    session_data = request.session.get('password_reset_otp')
    if not session_data:
        messages.error(request, "No active password reset request. Please request an OTP first.")
        return redirect('password_reset')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        pw1 = request.POST.get('new_password1', '')
        pw2 = request.POST.get('new_password2', '')

        # Basic validations
        if not entered_otp:
            messages.error(request, "Please enter the OTP.")
            return redirect('password_reset_verify')

        if pw1 != pw2 or not pw1:
            messages.error(request, "Passwords do not match or are empty.")
            return redirect('password_reset_verify')

        # Check expiry
        expires_at = session_data.get('expires_at')
        if expires_at is None or timezone.now().timestamp() > float(expires_at):
            _clear_otp_session(request)
            messages.error(request, "OTP expired. Please request a new one.")
            return redirect('password_reset')

        # Check OTP match
        if entered_otp != session_data.get('otp'):
            messages.error(request, "Invalid OTP.")
            return redirect('password_reset_verify')

        # OTP valid: set password for the user with that email if exists
        email = session_data.get('email')
        try:
            user = User.objects.get(email__iexact=email)
            user.set_password(pw1)
            user.save()
        except User.DoesNotExist:
            # If user doesn't exist, we still clear session and behave as successful to avoid enumeration
            pass

        _clear_otp_session(request)
        messages.success(request, "Password reset successful. You can now log in with your new password.")
        return redirect('login')

    # GET: render verify form
    return render(request, 'loginapp/password_reset_verify.html', {})


def password_reset_done(request):
    # Simple page to indicate flow completion (optional)
    return render(request, 'loginapp/password_reset_done.html', {})

=======
>>>>>>> e2f363d1db38133cafa260c091eb4d546218ad97
