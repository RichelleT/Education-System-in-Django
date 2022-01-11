from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_view(request, *args, **kwargs):
    return render(request, "landingpage.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def redir_view(request, *args, **kwargs):
    return render(request, "adminButtons.html", {})

def userProf_view(request, *args, **kwargs):
    return render(request, "userProfile.html", {})