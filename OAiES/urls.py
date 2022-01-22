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
from django.urls import path, include
from django.contrib.auth import views as auth_views

#import views from main component
from main.views import landing_view, login_view, redir_view, userProf_view, dashboard_view, sucess_view

#import views from testBuilder component
from testBuilder.views import addMod, modSel, addTests, modulePage, addQuiz, quizPage

#import views from other components
from registerAdmin.views import registerAdm
from registerUser.views import regisUsr_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('landing/', landing_view, name="landingP"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('userProf/', userProf_view, name="userProf"),
    path('dashboard/', dashboard_view, name="Dash"),
    path('moduleAdd/', addMod, name="addModule"),
    path('addTests/', addTests, name="addTest"),
    path('addQuizQ/', addQuiz, name="addQuiz"),
    path('moduleSel/', modSel, name="selModule"),
    path('modulePage/<str:pk>/', modulePage, name="modulePage"),
    path('quizPage/<str:pk>/', quizPage, name="quizPage"),
    path('redir/', redir_view), #REMOVE LATER
    path('sucess/', sucess_view),
    path('register/', registerAdm, name="Register"),
    path('registerUser/', regisUsr_view, name="RegisterUser"),
    path('admin/', admin.site.urls),
]
