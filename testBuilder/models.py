from django.db import models
from django.contrib.auth.models import User, Group

class Module(models.Model):
    module_name = models.CharField(max_length=120, default="")
    module_desc = models.CharField(max_length=300)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #participants = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self):
        return self.module_name

class addUserModule(models.Model):
    module_linked = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self):
        return self.module_linked


class Test(models.Model):
    test_name = models.CharField(max_length=100, default="")
    test_date = models.DateTimeField()
    module_sel = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.test_name

class Quiz(models.Model):
    ANSWER_CHOICES = (
            ('option1', 'option1'),
            ('option2', 'option2'),
            ('option3', 'option3'),
            ('option4', 'option4'),
        )
    test_sel = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=500, default="")
    op1 = models.CharField(max_length=300, default="")
    op2 = models.CharField(max_length=300, default="")
    op3 = models.CharField(max_length=300, default="")
    op4 = models.CharField(max_length=300, default="")
    answ = models.CharField(max_length=7, choices=ANSWER_CHOICES, blank=False, default='')
    # answ = models.CharField(
    #     max_length=300, 
    #     help_text="Input option1 for the first option, option2 for the second option",
    #     default=""
    # )

    def __str__(self):
        return self.quest

class quizResult(models.Model):
    linked_test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True) #linking result to test paper
    #linked_module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True) #linking result to quiz questions model
    attempted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    grade = models.CharField(max_length=10, default="")
    #a_time = models.DateTimeField()
    attempted_time = models.DateTimeField()

    def __str__(self):
        return str(self.attempted_by)

"""
class quizAttempt(models.Model):
    linked_test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    results_test = models.IntegerField()
    user_attempted = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nums_test_attempted = models.IntegerField()
    nums_test_passed = models.IntegerField()
    #numbers_correct = models.IntegerField()
    #test_percentage = models.IntegerField()

    def __str__(self):
        return self.user_attempted
"""

"""
class dashboard(models.Model):
    class_students #get all students in user list
    class_pass_rates #calculate pass rate
    module_num_test #number of tests for the module
"""