from django.shortcuts import render

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

def user_office(request):
    return render(request, "user_office.html")