from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, authenticate
from .models import PhoneNumbers
from .forms import SignUpForm
from django.core.exceptions import ObjectDoesNotExist


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            phone_ = form.cleaned_data.get('phone_number')
            try:
                my_record = PhoneNumbers.objects.get(phone_number=phone_, is_account_created=False)
            except ObjectDoesNotExist:
                return render(request, 'registration/signup.html', {'form': form})
            else:
                PhoneNumbers.objects.filter(phone_number=phone_).update(is_account_created=True)
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})