from django import forms

class AddPhoneForm(forms.Form):
    phone_number = forms.CharField(max_length=10, label="Номер телефону")