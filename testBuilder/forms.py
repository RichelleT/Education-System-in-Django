from django import forms
from testBuilder.models import Modules, Tests, QuestionsMod

class addModule(forms.ModelForm):
    class Meta:
        model = Modules
        fields = "__all__"

# class addModule(forms.Form):
#     class Meta:
#         model = Modules()
#         fields = ('module_name',
#         'module_desc')

#     def save(self, commit=True):
#         mod = super(addModule(), self).save(commit=False)
#         mod.module_name = self.cleaned_data['module_name']
#         mod.module_desc = self.cleaned_data['module_desc']

#         if commit:
#             mod.save()

#         return mod

class addTest(forms.Form):
    class Meta:
        model = Tests
        fields = "__all__" 

class addQuestionform(forms.ModelForm):
    class Meta:
        model=QuestionsMod
        fields="__all__"