from django.shortcuts import render
from django.http import HttpResponse
from registerUser.forms import RegistrationForm

# Create your views here.
def regisUsr_view(request, *args, **kwargs):
    return render(request, "registerUser.html", {})

def registerUsr(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registerUser.html', args)