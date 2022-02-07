from django.shortcuts import render
from django.http import HttpResponse

def regisUsr_view(request, *args, **kwargs):
    return render(request, "registerUser.html", {})