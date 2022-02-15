from django import forms
from testBuilder.models import Module, Test, Quiz, quizResult#, UserToModule

class addModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = (
            'module_name',
            'module_desc'
        )
        labels = {
            'module_name':'Enter Module Name',
            'module_desc':'Enter Module Description',
        }
# class addUser(forms.ModelForm):
#     class Meta:
#         model = UserToModule
#         fields = (
#             'participants',
#         )

class addTest(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            'test_name',
            'module_sel'
        )
        labels = {
            'test_name':'Enter Test Title',
            'module_sel':'Select Module',
        }

class addQuestions(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = (
            'test_sel',
            'quest',
            'op1',
            'op2',
            'op3',
            'op4',
            'answ',
            
        )
        labels  = {
            'test_sel':'Please Select Test Set', 
            'quest':'Input Question', 
            'op1':'Enter Answer Option 1',
            'op2':'Enter Answer Option 2',
            'op3':'Enter Answer Option 3',
            'op4':'Enter Answer Option 4',
            'answ':'Select Correct Answer',
        }
