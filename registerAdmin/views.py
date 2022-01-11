from django.shortcuts import  render, redirect
from registerAdmin.forms import RegistrationForm
# Create your views here.

# def regisAdm_view(request, *args, **kwargs):
#     return render(request, "registerAdmin.html", {})
def registerAdm(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registerAdmin.html', args)