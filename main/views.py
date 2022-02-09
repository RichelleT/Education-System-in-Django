from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from register.models import Profile

# Create your views here.
def landing_view(request, *args, **kwargs):
    return render(request, "landingpage.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def redir_view(request, *args, **kwargs):
    return render(request, "adminButtons.html", {})

def userProf_view(request):
    #users = User.objects.all().select_related('profile')
    prof = Profile.objects.filter(user=request.user)
    context = {
        "prof": prof,
    }
    return render(request, "userProfile.html", context)

def dashboard_view(request, *args, **kwargs):
    return render(request, "dashboard.html", {})

def sucess_view(request, *args, **kwargs):
    return render(request, "sucessPage.html", {})

#change html file to preview test UI
def test_view(request, *args, **kwargs):
    return render(request, "formStyle.html", {})