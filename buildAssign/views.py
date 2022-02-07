from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from registerUser.models import User
from buildAssign.models import Assignment
from buildAssign.forms import addAssignment
from main.decorators import group_required
import pdfplumber

@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
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

@login_required(login_url='/login/')
def atPage(request, pk):
    if request.method == 'POST':
        question = Assignment.objects.filter(linked_module=pk)
        user = request.user
    else: 
        questions = Assignment.objects.filter(linked_module=pk)

        context = {
            'questions': questions
        }
        return render(request, "assignPage.html", context)
