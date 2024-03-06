from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from accounts.models import PhoneNumbers
from datetime import datetime
from .models import Anon
from .forms import AddPhoneForm, AddAnonForm

# Create your views here.

@login_required
def index(request):
    return render(request, "main.html")

@login_required
def announcements(request):
    data = Anon.objects.all().order_by("-id").values()
    return render(request, "announcements.html", {"data" : data})

@login_required
def add_anon(request):
    if request.method == 'POST':
        form = AddAnonForm(request.POST, request.FILES)
        if form.is_valid():
            my_obj = Anon()

            cur_user = request.user
            my_obj.post_author = cur_user.username

            post_name = form.cleaned_data["post_name"]
            my_obj.post_name = post_name

            post_text = form.cleaned_data["post_text"]
            my_obj.post_text = post_text

            post_image = request.FILES.get("post_image")
            my_obj.post_image = post_image

            post_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            my_obj.post_date = post_date

            post_category = 1
            my_obj.post_category = post_category
            my_obj.save()
            return HttpResponseRedirect("/home_manager/announcements/")
    else:
        form = AddAnonForm()
    return render(request, "anon_form.html", context={"form" : form})

@login_required
def update_anon(request, id):
    my_obj = Anon.objects.get(id=id)
    if request.method == 'POST':
        form = AddAnonForm(request.POST, request.FILES)
        if form.is_valid():
            Anon.objects.get(id=id).post_image.delete(save=False)
            
            cur_user = request.user
            my_obj.post_author = cur_user.username

            post_name = form.cleaned_data["post_name"]
            my_obj.post_name = post_name

            post_text = form.cleaned_data["post_text"]
            my_obj.post_text = post_text

            post_image = request.FILES.get("post_image")
            my_obj.post_image = post_image

            post_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            my_obj.post_date = post_date

            post_category = 1
            my_obj.post_category = post_category
            my_obj.save()
            return HttpResponseRedirect("/home_manager/announcements/")
    else:
        form = AddAnonForm()
    return render(request, "anon_update.html", context={"form" : form})

@login_required
def del_anon(request, id):
    obj = Anon.objects.get(id=id)
    if request.method == "POST":
        Anon.objects.get(id=id).post_image.delete(save=False)
        obj.delete()
        return HttpResponseRedirect("/home_manager/announcements/")
    return render(request, "anon_del.html", context={"obj" : obj})

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
                obj.owner_id = ""
                obj.is_account_created = False
                obj.save()
                return HttpResponseRedirect('/home_manager/nums/')
    else:
        form = AddPhoneForm()
    return render(request, 'nums_form.html', {'form': form})

@login_required
def del_num(request, id):
    obj = PhoneNumbers.objects.get(id=id)
    username_ = obj.owner_id
    if request.method == "POST":
        try:
            user_obj = User.objects.get(username=username_)
        except User.DoesNotExist:
            obj.delete()
            return HttpResponseRedirect("/home_manager/nums/")
        else:
            user_obj.delete()
            obj.delete()
            return HttpResponseRedirect("/home_manager/nums/")
    return render(request, "nums_del.html", context={"nums" : obj})