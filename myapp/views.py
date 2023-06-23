# from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

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
class CandidateView(View):
   def get(self,request,pk):
      candidate=Resume.objects.get(pk=pk)
      return render(request,'myapp/candidate.html',{'candidate':candidate})
