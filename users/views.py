from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserLoginForm


# Создание регистрации
def register_view(request):
    if request.method == 'POST':
        # user ->username,....-> request UserRegisterForm
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Сохранить данные в БД username,email.password1
            form.save()
            username = form.cleaned_data.get('username')  # Sasha
            password = form.cleaned_data.get('password1')  # SashaDarkPrice2010
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        else:
            form = UserRegisterForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'signup.html', {'form': form})


# Функция для логина
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #Sasha
            password = form.cleaned_data.get('password1') #asfasd
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            form = UserLoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('home')
