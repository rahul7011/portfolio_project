from django.shortcuts import render
from .models import jobs

# Create your views here.

def home(request):
    job = jobs.objects.all()
    
    return render(request,'job/home.html',{'jobs':job})
