from email import message
from django.shortcuts import redirect, render
from .models import CustomUser
from django.views.generic.base import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
class Registration(TemplateView):
    template_name = 'app/register.html'
    
    def post(self,request):
        data = request.POST
        print(data)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = make_password(data['password'])
        DOB = data['dob']
        gender = data['gender']
        
        CustomUser.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,DOB=DOB,gender=gender)
        return redirect('login/')
    
class LoginView(TemplateView):
    template_name = 'app/login.html'

    def post(self, request):
        data = request.POST
        
        email = data['email']
        password = data['password']
        
        user = CustomUser.objects.filter(email=email)
        
        if user:
            authenticate(email=email,password=password)
            messages.success(request,"SuccessFully Login...")
            return redirect('userlist/')
        else:
            messages.error(request,"User with this email does'nt exists")   
            
class UserListView(TemplateView):
    template_name = 'app/userlist.html'  
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.all()
        return context

class UserUpdateView(TemplateView):
    template_name = 'app/editprofile.html'
    
    def get_context_data(self, id, **kwargs):
        context= super().get_context_data(**kwargs)
        context['id'] = CustomUser.objects.get(id=id)
        return context

        
    