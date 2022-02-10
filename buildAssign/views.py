from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from buildAssign.models import Assignment, Answer
from buildAssign.forms import addAssignment, addAnswer
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
            if form.host is None:
                form.host = host
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

def addAnsw(request):
    if request.method == 'POST':
        host = request.user
        current_datetime = datetime.datetime.now(tz=timezone.utc) 
        mod_form = addAnswer(request.POST)
        #module = Module.objects.get(pk=pk)

        if mod_form.is_valid(): #and add_form.is_valid():
            form = mod_form.save(commit=False)

            # if form.linked_assign is None:
            #     form.linked_assign = module

            if form.host is None:
                form.host = host

            if form.created_date is None:
                form.created_date = current_datetime

                form.save()
            return redirect('/sucess/')
    else:
        mod_form = addAnswer()

        args = {
            'mod_form': mod_form
        }
        return render(request, 'addAssignQ.html', args)


@login_required(login_url='/login/')
def atPage(request, pk):
    if request.method == 'POST':
        question = Answer.objects.filter(link_assign=pk)
        user = request.user
        for q in question:
            print(q.question)
            print(answer)
            userAnsw = request.POST.get(answer)
        

    else: 
        questions = Answer.objects.filter(link_assign=pk)

        context = {
            'questions': questions
        }
        return render(request, "assignPage.html", context)
