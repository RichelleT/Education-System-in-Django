from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from buildAssign.models import Assignment, Answer, AssignResult
from testBuilder.models import Module, Test, Quiz, quizResult#, UserToModule
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
            if form.created_by is None:
                form.created_by = host
            if form.created_date is None:
                form.created_date = current_datetime
                form.save()
            return redirect('/moduleSel/')
    else:
        mod_form = addAssignment()

        args = {
            'mod_form': mod_form
        }
        return render(request, 'addAssignment.html', args)

def addAnsw(request, pk):
    if request.method == 'POST':
        host = request.user
        current_datetime = datetime.datetime.now(tz=timezone.utc) 
        mod_form = addAnswer(request.POST)
        link = Assignment.objects.get(pk=pk)
        #module = Module.objects.get(pk=pk)

        if mod_form.is_valid(): #and add_form.is_valid():
            form = mod_form.save(commit=False)

            # if form.linked_assign is None:
            #     form.linked_assign = module
            if form.link_assign is None:
                form.link_assign = link

            if form.host is None:
                form.host = host

            if form.created_date is None:
                form.created_date = current_datetime

                form.save()
            return redirect('/moduleSel/')
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
        #module = Module.objects.get(pk=pk)
        ass = Assignment.objects.get(pk=pk)
        test = Answer.objects.get(link_assign=pk)

        score=0
        #wrong=0
        correct=0
        total=0

        user = request.user
        current_datetime = datetime.datetime.now(tz=timezone.utc)  

        for q in question:
            print(q.question)
            print(q.answer)
            oriAnsw = q.answer
            userAnsw = request.POST.get('my_textarea')
            print(userAnsw)
        
        oriL = list(oriAnsw.split())
        print("Original Answer Splited Lines:", oriL)
        print('Length:', len(oriL))
        userL = userAnsw.split()
        print("User Input Splited Line:", userL)
        print('Length:', len(userL))

        for l in oriL:
            total += 1 #works

        for m in oriL:
            for n in userL:
                if m == n: 
                    correct += 1
                    score += 10

        # if userL == oriL:
        #     correct += 1
        #     score += 10
        # else:
        #     wrong += 1

        percent = round(score/(total*10) * 100)

        if percent > 40:
            grade = "Pass"
        else:
            grade = "Fail"

        insert_to_db = AssignResult.objects.create(
            #linked_module=module,
            link_ques=test,
            correct=correct, 
            #wrong=wrong, 
            percentage=percent, 
            total=total,
            grade=grade,
            #linked_module=module,
            linked_assign=ass,
            attempted_time=current_datetime,
            attempted_by=user,
            #userAnsw=request.POST.get(q.quest),
        )

        context = {
            'score':score,
            'correct':correct,
            #'wrong':wrong,
            'percent':percent,
            'total':total,
            'grade': grade,
            'user': user,
            #'res':res,
        }
        return render(request,'assignResult.html',context)

    else: 
        questions = Answer.objects.filter(link_assign=pk)

        context = {
            'questions': questions
        }
        return render(request, "assignPage.html", context)

def aResultPg(request, pk):
    resList = AssignResult.objects.filter(linked_assign=pk)
    #module_title = Module.objects.get(pk=pk)
    test_title = Answer.objects.get(pk=pk)
    stuResList = AssignResult.objects.filter(attempted_by=request.user, linked_assign=pk)

    context = {
        'resList':resList,
        #'module_title': module_title,
        'test_title':test_title,
        'stuResList':stuResList,
    }
    return render(request, "fullAssignResult.html", context)
