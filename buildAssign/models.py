from django.db import models
from testBuilder.models import Module
from django.contrib.auth.models import User

class Assignment(models.Model):
    linked_module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=1000, default="")
    #must test if not working, remove answer field.
    answer = models.CharField(max_length=5000, default="")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    