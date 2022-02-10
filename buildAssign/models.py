from django.db import models
from testBuilder.models import Module
from django.contrib.auth.models import User

class Assignment(models.Model):
    linked_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=1000, default="")
    #must test if not working, remove answer field.
    answer = models.CharField(max_length=5000, default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.question

class AssignResult(models.Model):
    linked_assign = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True) #linking result to test paper
    linked_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True) #linking result to quiz questions model
    attempted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    correct = models.IntegerField(default=0)
    #wrong = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    grade = models.CharField(max_length=10, default="")
    a_time = models.DateTimeField(auto_now=True)
    attempted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.attempted_by)