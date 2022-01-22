from django.shortcuts import render
from django.http import HttpResponse
from registerUser.forms import addUserForm

# Create your views here.
def regisUsr_view(request, *args, **kwargs):
    return render(request, "registerUser.html", {})

def registerUsr(request):
    if request.method =='POST':
        form = addUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = addUserForm()

        args = {'form': form}
        return render(request, 'registerUser.html', args)