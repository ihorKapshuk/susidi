from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from accounts.models import PhoneNumbers
from .forms import AddPhoneForm

# Create your views here.

@login_required
def index(request):
    return render(request, "main.html")

@login_required
def announcements(request):
    return render(request, "announcements.html")

@login_required
def complaints(request):
    return render(request, "complaints.html")

@login_required
def lost(request):
    return render(request, "lost.html")

@login_required
def helpful(request):
    return render(request, "helpful.html")

@login_required
def user_office(request):
    cur_user = request.user
    my_name = cur_user.username
    return render(request, "user_office.html", context={"cur_name" : my_name})

@login_required
def nums_control(request):
    data = PhoneNumbers.objects.all().values()
    return render(request, "nums_control.html", context={"nums" : data})

@login_required
def add_num(request):
    if request.method == 'POST':
        form = AddPhoneForm(request.POST)
        if form.is_valid():
            phone_ = form.cleaned_data.get('phone_number')
            try:
                my_record = PhoneNumbers.objects.get(phone_number=phone_)
            except ObjectDoesNotExist:
                obj = PhoneNumbers()
                obj.phone_number = phone_
                obj.owner_id = -1
                obj.is_account_created = False
                obj.save()
                return HttpResponseRedirect('/home_manager/nums/')
    else:
        form = AddPhoneForm()
    return render(request, 'nums_form.html', {'form': form})

@login_required
def del_num(request, id):
    obj = PhoneNumbers.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/home_manager/nums/")
    return render(request, "nums_del.html", context={"nums" : obj})