from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
#from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from registerUser.models import User
from rest_framework import serializers, viewsets, routers

urlpatterns = [
  #path('auth/', include('rest_framework.urls')),
  path('auth/', include('rest_auth.urls')),
]