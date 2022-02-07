from rest_framework import serializers
from registerUser.models import  User
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)

class UserSerializer(serializers.ModelSerializer):
  role = GroupSerializer(many=True)
  class Meta:
      model = User
      fields = "__all__"