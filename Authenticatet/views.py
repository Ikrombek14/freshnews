from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Aslida, login qilganingizdan so'ng qayerga o'tishni xohlasangiz
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Parolni o'zgartirish
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Sessionni yangilash
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'password_change_done.html')



def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
