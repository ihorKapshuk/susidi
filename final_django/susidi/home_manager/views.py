from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from accounts.models import PhoneNumbers
from datetime import datetime
from .models import Anon, Comment
from .forms import AddPhoneForm, AddAnonForm, AddCommentForm

# Create your views here.

@login_required
def index(request):
    return render(request, "main.html")

@login_required
def announcements(request):
    data = Anon.objects.all().filter(post_category=1).order_by("-id").values()
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
        comments = Comment.objects.filter(com_post_id=id)
        for com in comments:
            com.com_image.delete(save=False)
            com.delete()
        Anon.objects.get(id=id).post_image.delete(save=False)
        obj.delete()
        return HttpResponseRedirect("/home_manager/announcements/")
    return render(request, "anon_del.html", context={"obj" : obj})

@login_required
def anon_com(requset, id, category):
    post_data = Anon.objects.filter(id=id)
    com_data = Comment.objects.all().filter(com_category=category, com_post_id=id).order_by("-id").values()
    context = {
        "post_data" : post_data,
        "com_data" : com_data
    }
    return render(requset, "anon_comments.html", context=context)

@login_required
def add_com(request, id, category):
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            my_obj = Comment()

            com_post_id = id
            my_obj.com_post_id = com_post_id

            cur_user = request.user
            my_obj.com_author = cur_user.username

            com_text = form.cleaned_data["com_text"]
            my_obj.com_text = com_text

            com_image = request.FILES.get("com_image")
            my_obj.com_image = com_image

            com_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            my_obj.com_date = com_date

            com_category = category
            my_obj.com_category = com_category
            my_obj.save()
            return HttpResponseRedirect(f"/home_manager/anon_com/{id}/{category}/")
    else:
        form = AddCommentForm()
    return render(request, "com_form.html", context={"form" : form})

@login_required
def update_com(request, id, this_post_id, category):
    my_obj = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            com_post_id = this_post_id
            my_obj.com_post_id = com_post_id

            cur_user = request.user
            my_obj.com_author = cur_user.username

            com_text = form.cleaned_data["com_text"]
            my_obj.com_text = com_text

            com_image = request.FILES.get("com_image")
            my_obj.com_image = com_image

            com_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            my_obj.com_date = com_date

            com_category = category
            my_obj.com_category = com_category
            my_obj.save()
            return HttpResponseRedirect(f"/home_manager/anon_com/{this_post_id}/{category}/")
    else:
        form = AddCommentForm()
    return render(request, "com_update.html", context={"form" : form})

@login_required
def del_com(request, id, this_post_id, category):
    obj = Comment.objects.get(id=id)
    if request.method == "POST":
        Comment.objects.get(id=id).com_image.delete(save=False)
        obj.delete()
        return HttpResponseRedirect(f"/home_manager/anon_com/{this_post_id}/{category}/")
    context = {
        "obj" : obj,
        "id" : this_post_id,
        "category" : category
    }
    return render(request, "com_del.html", context=context)

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