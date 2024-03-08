from django import forms
from .models import Anon

class AddPhoneForm(forms.Form):
    phone_number = forms.CharField(max_length=10, label="Номер телефону")

class AddAnonForm(forms.Form):
    post_name = forms.CharField(max_length=100, label="Назва посту")
    post_text = forms.CharField(max_length=250, label="Пост")
    post_image = forms.ImageField(label="", required=False)

class AddCommentForm(forms.Form):
    com_text = forms.CharField(max_length=250, label="Коментар")
    com_image = forms.ImageField(label="", required=False)