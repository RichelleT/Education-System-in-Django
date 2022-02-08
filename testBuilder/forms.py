from django import forms
from testBuilder.models import Module, Test, Quiz, quizResult, UserToModule

class addModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = (
            'module_name',
            'module_desc'
        )

class addUser(forms.ModelForm):
    class Meta:
        model = UserToModule
        fields = (
            'participants',
        )

class addTest(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            'test_name',
            'module_sel'
        )

class addQuestions(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__" 
