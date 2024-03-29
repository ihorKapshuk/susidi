from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10, help_text='Починаючи з 0 (10 цифр).', label="Номер телефону")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )