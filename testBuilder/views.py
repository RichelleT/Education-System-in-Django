from django.shortcuts import  render, redirect
from django.http import HttpResponse
from testBuilder.forms import addModule, addTest
from testBuilder.models import Modules, Tests

# Create your views here.
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
    modlist = Modules.objects.all()
    return render(request, "moduleSelect.html", {'modlist':modlist})