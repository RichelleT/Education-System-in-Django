from django.db import models

# Create your models here.
class Modules(models.Model):
    module_name = models.CharField(max_length=120)
    module_desc = models.CharField(max_length=300)

class Tests(models.Model):
    test_name = models.CharField(max_length=100)
    test_date = models.DateTimeField()