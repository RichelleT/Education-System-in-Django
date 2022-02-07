from django.db import models
from django.contrib.auth.models import AbstractUser, Group

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(_('email address'), unique = True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['username', 'email', 'first_name', 'last_name']
  
  def __str__(self):
      return "{}".format(self.username)