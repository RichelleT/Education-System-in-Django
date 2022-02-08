from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_faculty = models.TextField(max_length=500, blank=True, default="")
    programme = models.CharField(max_length=30, blank=True, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, default='M')
    #birth_date = models.DateField(null=True, blank=True)
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""