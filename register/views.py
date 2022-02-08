from django.shortcuts import  render, redirect
from register.forms import RegistrationForm, ExtendedForm
from django.contrib import messages
from django.db import transaction

"""
def registerAdm(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userProf/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registerAdmin.html', {})
"""

@transaction.atomic
def registerUsr(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ExtendedForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            profile = profile_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = new_user.id
                profile.save()
            return redirect('/userProf/')
        else:
            print("Error. Try Again.")
    else:
        user_form = RegistrationForm()
        profile_form = ExtendedForm()
    return render(request, 'registerUser.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
