from django.db import models
from testBuilder.models import Module
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django_quill.fields import QuillField
from tinymce import models as tinymce_models

class Assignment(models.Model):
    linked_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    assign_name = models.CharField(max_length=1000, default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField()
    set_added = models.BooleanField(default=False)

    def __str__(self):
        return self.assign_name

class Answer(models.Model):
    link_assign = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #question = models.TextField(max_length=5000, default="")
    answer = models.CharField(max_length=5000, default="")
    question = tinymce_models.HTMLField()
    #answer = QuillField()
    created_date = models.DateTimeField()
    #set_added = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class File(models.Model):
    link_answ = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    upload_txt = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['txt'] ) ])
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link_assign = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.question + " " + self.uploader


class AssignResult(models.Model):
    link_ques = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True) 
    linked_assign = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    attempted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    correct = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    grade = models.CharField(max_length=10, default="")
    lettergrade = models.CharField(max_length=10, default="")
    attempted_time = models.DateTimeField()

    def __str__(self):
        return str(self.attempted_by)