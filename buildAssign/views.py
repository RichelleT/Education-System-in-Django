from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from buildAssign.models import Assignment
from buildAssign.forms import addAssignment

@login_required(login_url='/login/')
def addAssign(request):
    if request.method =='POST':
        form = addAssignment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucess/')
    else:
        form = addAssignment()

        args = {
            'form': form
        }
        return render(request, 'addAssignment.html', args)