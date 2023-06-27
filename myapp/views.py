# from django.shortcuts import render

# Create your views here.
from email import message
from tabnanny import check
from urllib import response
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

# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .helper import send_forget_password_mail
# import uuid

# def ForgetPage(request):
#     print(".............")
#     if request.method == 'POST':
#         print(">>>>>>>>>>>")
#         username = request.POST.get('username')
#         if not User.objects.filter(username=username).exists():
#             messages.error(request, 'No user found')
#             print("checking................")
#             return render(request, 'forget.html')

        
#         user_obj = User.objects.get(username=username)
#         print("chedking 2....")
#         token = str(uuid.uuid4())
#         print(".........<<<<<<<<<<<")
#         send_forget_password_mail(user_obj.email)
#         print("cheming 4..................")
#         messages.success(request, 'An email has been sent')
#         print("code run..................................")
#         return redirect('login')
#     print("chckeing 3....")
#     return render(request,'myapp/forgetpassword.html')

# def Conform_password(request):
#     if request.method == 'POST':
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('conform_password')
#         if password1 == password2:
#             print("Update password")
#             # Assuming you have a unique identifier like email or username
#             user_obj = User.objects.get(username=request.user.username)
#             user_obj.set_password(password2)  # Set the new password
#             user_obj.save()  # Save the updated user object
#             return redirect('login')
#         else:
#             print("Password mismatch")
#     return render(request, 'myapp/conform_password.html')



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .helper import send_forget_password_mail
import uuid
def ForgetPage(request):
    print("enter in forget......")
    if request.method == 'POST':
        username = request.POST.get('username')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'No user found')
            return render(request, 'myapp/forgetpassword.html')

        user_obj = User.objects.get(username=username)
        token = str(uuid.uuid4())
        print("token",token)
        
        # Create a new Profile object if it doesn't exist
        if not hasattr(user_obj, 'profile'):
            Profile.objects.create(user=user_obj)

        profile = user_obj.profile  # Retrieve the associated profile
        print("profile",profile)
        profile.forget_token = token
        profile.save()
        send_forget_password_mail(user_obj.email, token)
        messages.success(request, 'An email has been sent')
        return redirect('login')

    return render(request, 'myapp/forgetpassword.html')


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
import uuid

def ConformPasswordPage(request):
    print("enter in conform password...........")
    token = request.GET.get('token')
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('conform_password')
        print(password1, password2, token)
        print('token', token)
        try:
            print("enter in try......")
            if token is not None:
                profile = Profile.objects.get(forget_token=token)
                print('profile is ......', profile)
                user_obj = profile.user  # Retrieve the associated user
                print("user_obj", user_obj)
                if password1 == password2:
                    print("password match.....")
                    user_obj.set_password(password2)
                    profile.forget_token = ''
                    user_obj.save()
                    profile.save()
                    print("profile save.....")
                    messages.success(request, 'Password updated successfully')
                    return redirect('login')
                else:
                    print("password mismatch.......")
                    messages.error(request, 'Password mismatch')
            else:
                print("No token provided.")
                messages.error(request, 'Invalid token')
        except Profile.DoesNotExist:
            print("except block working.....")
            messages.error(request, 'Invalid token')
    else:
        if token is None:
            messages.error(request, 'Token not provided')
            return redirect('login')  # Redirect to login page if token is not provided
        
    return render(request, 'myapp/conform_password.html', {'token': token})
