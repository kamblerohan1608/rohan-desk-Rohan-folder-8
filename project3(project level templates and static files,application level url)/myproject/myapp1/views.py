from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp1/home.html')

def services(request):
    return render(request,'myapp1/services.html')