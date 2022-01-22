from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from testBuilder.forms import addModule, addTest, addQuestions
from testBuilder.models import Module, Test, Quiz

def addMod(request):
    if request.method =='POST':
        form = addModule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucess/')
    else:
        form = addModule()

        args = {'form': form}
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

        context = {'form': form}
        return render(request, 'addTest.html', context)

def modulePage(request, pk):
    modPage = Module.objects.filter(id=pk)
    mtLst = Test.objects.filter(module_sel=pk)

    context = {'modPage':modPage, 'mtLst':mtLst}
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

        context = {'form': form}
        return render(request, "addQuiz.html", context)

def quizPage(request, pk):
    quizPg = Quiz.objects.filter(test_sel=pk)

    context = {'quizPg': quizPg}
    return render(request, "quizPage.html", context)