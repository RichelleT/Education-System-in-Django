from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from testBuilder.forms import addModule, addTest, addQuestions
from testBuilder.models import Module, Test, Quiz, quizResult
from django.db.models import F
from django.contrib.auth.models import User

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

def modSel(request, *args, **kwargs):
    modlist = Module.objects.all()
    return render(request, "moduleSelect.html", {'modlist':modlist})

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

def qrPage(request, pk):
    if request.method == 'POST': #render results page
        print(request.POST)
        questions = Quiz.objects.filter(test_sel=pk)
        user = quizResult.objects.filter(id=pk)
        #quizID = quizResult.objects.filter(id=pk)
        """score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }"""
        scr = quizResult.objects.get(score)
        cor = quizResult.objects.get(correct)
        wrg = quizResult.objects.get(wrong)
        ttl = quizResult.objects.get(total)
        percent = quizResult.objects.get(percentage)
        for q in questions:
            ttl.total += 1
            ttl.save()
            print(request.POST.get(q.quest))
            print(q.answ)
            if q.answ ==  request.POST.get(q.quest):
                cor.correct += 1
                scr.score += 1
                cor.save() 
                scr.save()               
            else:
                wrg.wrong += 1
                wrg.save()
        percent.percentage = scr/(ttl*10) *100

        context = {
            'scr': scr,
            'cor': cor,
            'wrg': wrg,
            'ttl': ttl,
            'percent': percent
        }
        return render(request,'resultPage.html',context)

    else: #render quiz page
        questions = Quiz.objects.filter(test_sel=pk)

        context = {
            'questions': questions
        }
        return render(request, "quizPage.html", context)

"""
get linked test - pk
get linked user - pk

"""
"""
if q.answ ==  request.POST.get(q.quest):
    correct = quizResult.objects.update(correct=+1)
    score = quizResult.objects.update(score=+10)
else:
    wrong = quizResult.objects.update(wrong=+1)
percent = quizResult.objects.update(percentage=+1) 
"""