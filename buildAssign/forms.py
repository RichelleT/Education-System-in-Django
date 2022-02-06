from django import forms
from buildAssign.models import Assignment

class addAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"