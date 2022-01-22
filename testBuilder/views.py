from django.shortcuts import  render, redirect
from django.http import HttpResponse
from testBuilder.forms import addModule, addTest, addQuestions
from testBuilder.models import Module, Test, Quiz

def addMod(request):
    if request.method =='POST':
        form = addModule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/moduleSel/')
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
            return redirect('/moduleSel/')
    else:
        form = addTest()

        context = {'form': form}
        return render(request, 'addTest.html', context)
