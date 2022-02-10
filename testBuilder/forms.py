from django import forms
from testBuilder.models import Module, Test, Quiz, quizResult#, UserToModule

class addModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = (
            'module_name',
            'module_desc'
        )

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

class addQuestions(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__" 
        labels  = {
            'test_sel':'Please Select Test Set', 
            'quest':'Input Question', 
            'op1':'Enter Answer Option 1',
            'op2':'Enter Answer Option 2',
            'op3':'Enter Answer Option 3',
            'op4':'Enter Answer Option 4',
            'answ':'Select Correct Answer',
        }
