from django.shortcuts import  render, redirect
from django.http import HttpResponse
from registerUser.forms import RegistrationForm
from registerUser.serializers import UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

"""
def registerUser(request):
    if request.method =='POST':
        form = UserSerializer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = UserSerializer()

        context = {'form': form}
        return render(request, 'registerUser.html', context)

"""

def registerUser(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = RegistrationForm()

        context = {'form': form}
        return render(request, 'registerUser.html', context)

