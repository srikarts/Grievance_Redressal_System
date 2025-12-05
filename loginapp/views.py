from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile

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

