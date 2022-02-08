from rest_framework import serializers
from registerUser.models import  User
from django.contrib.auth.models import Group
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', 'id')

class UserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True)
  username = serializers.CharField(required=True)
  #password = serializers.CharField(write_only=True,required=True,help_text='Leave empty if no change needed',style={'input_type': 'password', 'placeholder': 'Password'})
  #password = serializers.CharField(min_length=8, write_only=True)
  #password2 = serializers.CharField(min_length=8, write_only=True)
  first_name = serializers.CharField()
  last_name = serializers.CharField()
  #groups = GroupSerializer(many=True)
  #groups = GroupSerializer()
  class Meta:
      model = User
      fields = (
             'email',
             'username', 
             'password', 
             #'password2', 
             'first_name', 
             'last_name', 
             'groups', 
             'programme_name', 
             'school_faculty', 
             'gender',
         )
      extra_kwargs = {
          'email': {'write_only':True},
          'username': {'write_only':True},
          'password': {'write_only':True}
        }

  """def validate_password(self, value):
    try:
        validate_password(value)
    except ValidationError as exc:
        raise serializers.ValidationError(str(exc))
    return value"""

  def create(self, validated_data):
    return User.objects.create(**validated_data)

  def update(self, instance, validated_data):
      user = super().update(instance, validated_data)
      if 'password' in validated_data:
          user.set_password(validated_data['password'])
          user.save()
      return user

"""
ISSUE - cannot login, try other validation methods; maybe email validation issue
TRY
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
"""

"""
  def create(self, validated_data):
      user = super().create(validated_data)
      userN = User(
          username=validated_data['username'],
      )
      email = User(email=validated_data['email'])
      user.set_password(validated_data['password'])

      user.is_active = False
      user.save()
      return user
  """

"""
  def create(self, validated_data):
      user = User(
          username=validated_data['username'],
      )
      user.set_password(validated_data['password'])
      user.save()
      return user
"""