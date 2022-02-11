from django import forms
from buildAssign.models import Assignment, Answer, File

class addAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = (
            'linked_module',
            'assign_name',
            #'question',
            #'answer',
        )
        labels = {
            'linked_module':'Select Module',
            'assign_name':'Add Assignment Title',
            #'question':'Input Question',
            #'answer':'Input Answer Keywords',
        }

class addAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            #'link_assign',
            #'assign_name',
            'question',
            'answer',
        )
        labels = {
            #'link_assign':'Select Assignment Set',
            #'assign_name':'Add Assignment Title',
            'question':'Input Question',
            'answer':'Input Answer Keywords',
        }

class fileUpload(forms.ModelForm):
    class Meta:
        model = File
        fields = (
            'upload_txt',
        )