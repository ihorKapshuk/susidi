from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "main.html")

def announcements(request):
    return render(request, "announcements.html")

def complaints(request):
    return render(request, "complaints.html")

def lost(request):
    return render(request, "lost.html")

def helpful(request):
    return render(request, "helpful.html")

@login_required
def user_office(request):
    cur_user = request.user
    my_name = cur_user.username
    return render(request, "user_office.html", context={"cur_name" : my_name})