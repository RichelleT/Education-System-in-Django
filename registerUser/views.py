from django.shortcuts import  render, redirect
from django.http import HttpResponse
from registerUser.forms import RegistrationForm
from registerUser.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from registerUser.models import User
from django.contrib.auth.models import Group
from .serializers import UserSerializer


class UserRegis(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    #permission_classes = [IsAuthenticated]
    template_name = 'registerUser.html'

    def get(self, request, format=None):
        serializer=UserSerializer()
        return Response({'serializer':serializer})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer':serializer})
        serializer.save()
        return redirect('/userProf/')


"""
def registerUser(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)

        a = Group.objects.get(name='Admin') #3
        e = Group.objects.get(name='Educator') #1
        s = Group.objects.get(name='Student') #2
        role_sel = request.POST['role']
        #print(role_sel)
        #users = User.objects.all()
        if form.is_valid():
            #for u in users:
            if role_sel == 1:
                UserSerializer.roles.set(e)
            elif role_sel == 2:
                UserSerializer.roles.set(e)
                #role.groups.set(s)
            else:
                UserSerializer.roles.set(a)
                #User.groups.set(a)
            form.save()
            return redirect('/userProf/')
    else:
        form = RegistrationForm()

        context = {'form': form}
        return render(request, 'registerUser.html', context)
"""