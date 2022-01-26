from django import forms
from testBuilder.models import Module, Test, Quiz, quizResult

class addModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = "__all__"

class addTest(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__" 

class addQuestions(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__" 
