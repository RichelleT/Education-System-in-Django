from django import forms
from buildAssign.models import Assignment

class addAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = (
            'linked_module',
            'question',
            'answer',
        )
        labels = {
            'linked_module':'Select Module',
            'question':'Input Question',
            'answer':'Input Answer Keywords',
        }