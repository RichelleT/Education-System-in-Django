from django.shortcuts import render
from django.http import HttpResponse
#from registerUser.forms import addUserForm

def regisUsr_view(request, *args, **kwargs):
    return render(request, "registerUser.html", {})