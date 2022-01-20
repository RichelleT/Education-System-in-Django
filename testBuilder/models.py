from django.db import models

# Create your models here.
class Modules(models.Model):
    module_name = models.CharField(max_length=120)
    module_desc = models.CharField(max_length=300)

class Tests(models.Model):
    test_name = models.CharField(max_length=100)
    test_date = models.DateTimeField()

class QuestionsMod(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question