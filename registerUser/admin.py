from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from registerUser.models import User
from registerUser.forms import RegistrationForm

class UserAdmin(BaseUserAdmin):
  form = RegistrationForm
  fieldsets = (
      (None, {'fields': ('username', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      #(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('programme_name', 'school_faculty', 'gender')}),
  )
  """add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )"""
  list_display = ['username', 'first_name', 'last_name', 'programme_name', 'school_faculty']
  search_fields = ('username', 'first_name', 'last_name')
  ordering = ('username', )
admin.site.register(User, UserAdmin)
