from django import forms
# Вызываем готовый модель для Пользователя
from django.contrib.auth.models import User
# Это нужно для создании пользователя(Это готовая переманная)
from django.contrib.auth.forms import UserCreationForm


# форма для регистрации
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']


# форма для логина
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #******

