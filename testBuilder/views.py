from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from testBuilder.forms import addModule, addTest, addQuestions
from testBuilder.models import Module, Test, Quiz, quizResult
from django.db.models import F
from django.contrib.auth.models import User, Group

@login_required(login_url='/login/')
def addMod(request):
    if request.method =='POST':
        form = addModule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucess/')
    else:
        form = addModule()

        args = {
            'form': form
        }
        return render(request, 'addModule.html', args)

@login_required(login_url='/login/')
def modSel(request, *args, **kwargs):
    modlist = Module.objects.all()
    return render(request, "moduleSelect.html", {'modlist':modlist})

@login_required(login_url='/login/')
def addTests(request):
    if request.method =='POST':
        form = addTest(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucess/')
    else:
        form = addTest()

        context = {
            'form': form
        }
        return render(request, 'addTest.html', context)

@login_required(login_url='/login/')
def modulePage(request, pk):
    modPage = Module.objects.filter(id=pk)
    mtLst = Test.objects.filter(module_sel=pk)

    context = {
        'modPage':modPage,
        'mtLst':mtLst
    }
    return render(request, "modulePage.html", context)
    #filter() returns a queryset (which is iterable)
    #get() returns a single object (which is not iterable)
    
@login_required(login_url='/login/')
def addQuiz(request):
    if request.method == 'POST':
        form = addQuestions(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucess/')
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
        score=0
        wrong=0
        correct=0
        total=0
        user = request.user
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

        insert_to_db = quizResult.objects.create(
            correct=correct, 
            wrong=wrong, 
            percentage=percent, 
            total=total,
            grade=grade,
            #linked_module=module,
            #linked_test=test,
            attempted_by=user
        )

        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'grade': grade,
            'user': user,
            #'form':form
        }
        return render(request,'generateResult.html',context)
        #return render(request, "resultPage.html", context)

    else: #render quiz page
        questions = Quiz.objects.filter(test_sel=pk)

        context = {
            'questions': questions
        }
        return render(request, "quizPage.html", context)
