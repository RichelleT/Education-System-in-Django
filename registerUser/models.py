from django.db import models
from django.contrib.auth.models import AbstractUser, Group
#from registerUser.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from OAiES import settings

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
#User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    username = models.CharField(max_length = 50, blank=False, null=True, unique=True)
    email = models.EmailField(_('email address'), unique = True, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=False)
    #use default='M' if gender field has default issues
    #role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=False)
    #role = models.ForeignKey('auth.Group', related_name='group', on_delete=models.SET_NULL, null=True)
    programme_name = models.CharField(max_length=50, default="", blank=False, null=True)
    school_faculty = models.CharField(max_length=50, default="", blank=False, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    #REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    def __str__(self):
        return self.username

"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
"""