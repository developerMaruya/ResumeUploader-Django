# from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# without login page not open so 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates=Resume.objects.all()
        return render(request, 'myapp/home.html', {'form': form,'candidates':candidates})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        return render(request, 'myapp/home.html', {'form': form})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CandidateView(View):
   def get(self,request,pk):
      candidate=Resume.objects.get(pk=pk)
      return render(request,'myapp/candidate.html',{'candidate':candidate})


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and Conform password are not Same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'myapp/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username and password is incorrect !!")
    return render(request,'myapp/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')