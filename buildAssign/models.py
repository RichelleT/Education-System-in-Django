from django.db import models
from testBuilder.models import Module
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Assignment(models.Model):
    # LIMIT_CHOICES = (
    #     ('1', '1'),
    #     ('0', '0'),
    # )

    linked_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    assign_name = models.CharField(max_length=1000, default="")
    #must test if not working, remove answer field.
    #answer = models.CharField(max_length=5000, default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField()
    #limit = models.CharField(max_length=1, choices=LIMIT_CHOICES, blank=False, default='1')

    def __str__(self):
        return self.assign_name

class Answer(models.Model):
    link_assign = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.TextField(max_length=5000, default="")
    answer = models.TextField(max_length=5000, default="")
    created_date = models.DateTimeField()
    #upload_txt = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['txt'] ) ])

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
    #linked_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True) 
    attempted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    correct = models.IntegerField(default=0)
    #wrong = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    grade = models.CharField(max_length=10, default="")
    #a_time = models.DateTimeField(auto_now=True)
    attempted_time = models.DateTimeField()

    def __str__(self):
        return str(self.attempted_by)