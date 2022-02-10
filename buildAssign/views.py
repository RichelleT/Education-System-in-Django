from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from buildAssign.models import Assignment
from buildAssign.forms import addAssignment
from main.decorators import group_required
import pdfplumber
import shlex
import datetime
from django.utils import timezone

@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
def addAssign(request):
    if request.method =='POST':
        host = request.user
        current_datetime = datetime.datetime.now(tz=timezone.utc) 
        mod_form = addAssignment(request.POST)
        if mod_form.is_valid(): #and add_form.is_valid():
            form = mod_form.save(commit=False)
            if form.created_by is None:
                form.created_by = host
            if form.created_date is None:
                form.created_date = current_datetime
                form.save()
            return redirect('/sucess/')
    else:
        mod_form = addAssignment()

        args = {
            'mod_form': mod_form
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
