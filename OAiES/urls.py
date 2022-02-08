from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

#import views from main component
from main.views import landing_view, login_view, redir_view, userProf_view, dashboard_view, sucess_view

#import views from testBuilder component
from testBuilder.views import addMod, modSel, addTests, modulePage, addQuiz, qrPage

from buildAssign.views import addAssign

#import views from other components
from registerAdmin.views import registerAdm
#from registerUser.views import regisUsr_view#, registerUsr

urlpatterns = [
    #main page
    path('', landing_view, name='landing'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('landing/', landing_view, name="landingP"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('userProf/', userProf_view, name="userProf"),
    path('dashboard/', dashboard_view, name="Dash"),
    path('moduleAdd/', addMod, name="addModule"),
    path('addTests/', addTests, name="addTest"),
    path('addQuizQ/', addQuiz, name="addQuiz"),
    path('addAssignment/', addAssign, name="addAssign"),
    path('moduleSel/', modSel, name="selModule"),
    path('modulePage/<str:pk>/', modulePage, name="modulePage"),
    path('quizPage/<str:pk>/', qrPage, name="quizPage"),
    #path('resultPage/', qrPage, name="resultPage"),
    path('redir/', redir_view), #REMOVE LATER
    path('sucess/', sucess_view),
    path('register/', registerAdm, name="Register"),
    #path('registerUser/', regisUsr_view, name="RegisterUser"),
    #path('registerUser/', registerUsr, name="RegisterUser"),
    path('admin/', admin.site.urls),
]
