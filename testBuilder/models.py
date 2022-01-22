from django.db import models

class Module(models.Model):
    module_name = models.CharField(max_length=120, default="")
    module_desc = models.CharField(max_length=300)

    def __str__(self):
        return self.module_name

class Test(models.Model):
    test_name = models.CharField(max_length=100, default="")
    test_date = models.DateTimeField(auto_now_add=True)
    module_sel = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.test_name

class Quiz(models.Model):
    test_sel = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    quest = models.CharField(max_length=500)
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)
    answ = models.CharField(max_length=300)

    def __str__(self):
        return self.quest    