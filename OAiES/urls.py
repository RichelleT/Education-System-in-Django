"""OAiES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import landing_view
from main.views import login_view
from main.views import redir_view
from main.views import userProf_view
from main.views import dashboard_view
from registerAdmin.views import register
from registerUser.views import regisUsr_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('landing/', landing_view, name="landingP"),
    path('login/', login_view, name="login"),
    path('userProf/', userProf_view, name="userProf"),
    path('dashboard/', dashboard_view, name="Dash"),
    path('redir/', redir_view), #REMOVE LATER
    path('register/', register, name="Register"),
    path('registerUser/', regisUsr_view, name="RegisterUser"),
    path('admin/', admin.site.urls),
]
