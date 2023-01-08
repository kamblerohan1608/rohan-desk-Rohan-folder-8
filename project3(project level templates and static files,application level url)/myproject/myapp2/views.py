from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'myapp2/contact.html')

def about(request):
    return render(request,'myapp2/about.html')