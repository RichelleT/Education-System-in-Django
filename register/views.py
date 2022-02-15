from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.decorators import group_required
from register.forms import RegistrationForm, ExtendedForm
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import Group, User
from register.models import Profile

@transaction.atomic
# @login_required(login_url='/login/')
# @group_required('Admin', login_url='/login/')
def registerUsr(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ExtendedForm(request.POST)

        role_assign = request.POST.get('role')

        adm_group = Group.objects.get(id=1) 
        edu_group = Group.objects.get(id=2) 
        stu_group = Group.objects.get(id=3) 

        print("Assigned Role:", role_assign)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()

            profile = profile_form.save(commit=False)
            if role_assign == 'A':
                new_user.groups.add(adm_group)
            elif role_assign == 'E':
                new_user.groups.add(edu_group)
            elif role_assign == 'S':
                new_user.groups.add(stu_group)

            if profile.user_id is None:
                profile.user_id = new_user.id
                profile.save()
            return redirect('/landing/')
        else:
            print("Error. Try Again.")
    else:
        user_form = RegistrationForm()
        profile_form = ExtendedForm()
    return render(request, 'registerUser.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
