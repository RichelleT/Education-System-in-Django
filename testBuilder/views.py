from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from testBuilder.forms import addModule, addTest, addQuestions#, addUser
from testBuilder.models import Module, Test, Quiz, quizResult#, UserToModule
from django.db.models import F
from django.contrib.auth.models import User, Group
from main.decorators import group_required
import datetime
from django.utils import timezone
from buildAssign.models import Assignment, AssignResult, Answer

@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
def addMod(request):
    if request.method =='POST':

        host = request.user

        mod_form = addModule(request.POST)
        #add_form = addUser(request.POST)

        if mod_form.is_valid(): #and add_form.is_valid():
            form = mod_form.save(commit=False)
            if form.host is None:
                form.host = host
                form.save()
            #add_form.save()
            return redirect('/addTests/')
    else:
        mod_form = addModule()
        #add_form = addUser()

        args = {
            'mod_form': mod_form,
            #'add_form': add_form,
        }
        return render(request, 'addModule.html', args)

"""
@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
def addUserToMod(request):
    if request.method =='POST':
        add_form = addUserModule(request.POST)

        if add_form.is_valid():
            add_form.save()
        return
"""

@login_required(login_url='/login/')
def modSel(request, *args, **kwargs):
    modlist = Module.objects.all()
    
    return render(request, "moduleSelect.html", {'modlist':modlist})

@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
def addTests(request):
    if request.method =='POST':
        current_datetime = datetime.datetime.now(tz=timezone.utc) 
        host = request.user
        
        form = addTest(request.POST)

        if form.is_valid():
            #old_form.save()
            old_form = form.save(commit=False)

            if form.host is None:
                form.host = host
            if old_form.test_date is None:
                old_form.test_date = current_datetime
                old_form.save()
            return redirect('/addQuizQ/')
    else:
        form = addTest()

        context = {
            'form': form
        }
        
        return render(request, "addTest.html", context)


@login_required(login_url='/login/')
def modulePage(request, pk):
    modPage = Module.objects.filter(id=pk)
    mtLst = Test.objects.filter(module_sel=pk)
    #resList = quizResult.objects.filter(linked_module=pk)
    assignList = Assignment.objects.filter(linked_module=pk)
    #quesList = Answer.objects.filter(pk=pk)

    context = {
        'modPage':modPage,
        'mtLst':mtLst,
        'assignList': assignList,
        'quesList': quesList,
    }
    return render(request, "modulePage.html", context)
    #filter() returns a queryset (which is iterable)
    #get() returns a single object (which is not iterable)
    
@login_required(login_url='/login/')
@group_required('Educator', login_url='/login/')
def addQuiz(request):
    if request.method == 'POST':
        form = addQuestions(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addQuizQ/')
            #add page redir
    else:
        form = addQuestions()

        context = {
            'form': form
        }
        return render(request, "addQuiz.html", context)

@login_required(login_url='/login/')
def qrPage(request, pk):
    if request.method == 'POST': #render results page
        print(request.POST)
        questions = Quiz.objects.filter(test_sel=pk)
        test = Test.objects.get(pk=pk)
        module = Module.objects.get(pk=pk)
        #res = quizResult.objects.get(pk=pk)
        print(test)
        print(module)
        score=0
        wrong=0
        correct=0
        total=0
        user = request.user
        current_datetime = datetime.datetime.now(tz=timezone.utc)  
        for q in questions:
            total+=1
            #print(request.POST.get(q.test_sel.test_name))
            print(request.POST.get(q.quest))
            print(q.answ)
            if q.answ ==  request.POST.get(q.quest):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = round(score/(total*10) * 100)
        if percent > 40:
            grade = "Pass"
        else:
            grade = "Fail"
        
        if percent >= 90:
            lettergrade = "A+"
        elif percent >= 85:
            lettergrade = "A"
        elif percent >= 80:
            lettergrade = "A-"
        elif percent >= 75:
            lettergrade = "B+"
        elif percent >= 70:
            lettergrade = "B+"
        elif percent >= 65:
            lettergrade = "B+"
        elif percent >= 60:
            lettergrade = "C+"
        elif percent >= 55:
            lettergrade = "C"
        elif percent >= 50:
            lettergrade = "C-"
        elif percent >= 45:
            lettergrade = "D+"
        elif percent <= 40:
            lettergrade = "F"

        insert_to_db = quizResult.objects.create(
            linked_module=module,
            linked_test=test,
            correct=correct, 
            wrong=wrong, 
            percentage=percent, 
            total=total,
            grade=grade,
            lettergrade=lettergrade, 
            #linked_module=module,
            attempted_time=current_datetime,
            attempted_by=user,
            #userAnsw=request.POST.get(q.quest),
        )

        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'grade': grade,
            'user': user,
            #'res':res,
        }
        return render(request,'generateResult.html',context)
        #return render(request, "resultPage.html", context)

    else: #render quiz page
        questions = Quiz.objects.filter(test_sel=pk)

        context = {
            'questions': questions
        }
        return render(request, "quizPage.html", context)

def resultPg(request, pk):
    resList = quizResult.objects.filter(linked_module=pk)
    module_title = Module.objects.get(pk=pk)
    test_title = Test.objects.get(pk=pk)
    stuResList = quizResult.objects.filter(attempted_by=request.user, linked_module=pk)

    context = {
        'resList':resList,
        'module_title': module_title,
        'test_title':test_title,
        'stuResList':stuResList,
    }
    return render(request, "viewResultsPage.html", context)
    #return render(request, "viewResultsPageV2.html", context)
    #return render(request, "viewResultsPageV3.html", context)

# def studentResult(request, pk):
#     resList = quizResult.objects.filter(attempted_by=pk)
#     module_title = Module.objects.get(pk=pk)
#     test_title = Test.objects.get(pk=pk)

#     context = {
#         'resList':resList,
#     }
#     return render(request, "studentResult.html", context)