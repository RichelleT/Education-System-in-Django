from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

GENDER_SELECT = [
    ('female', 'Female'),
    ('male', 'Male'),
]

ROLE_SELECT = [
    ('administrator', 'Administrator'),
    ('educator', 'Educator'),
    ('student', 'Student'),
]

class addUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField(
        required=True,
        widget=forms.Select(choices=GENDER_SELECT)
    )
    role = forms.CharField(
        required=True,
        widget=forms.Select(choices=ROLE_SELECT)        
    )


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

#add roles