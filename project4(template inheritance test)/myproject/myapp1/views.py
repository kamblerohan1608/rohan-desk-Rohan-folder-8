from django.shortcuts import render

# Create your views here.

def home(request):
    data={'languages':['PYTHON','JAVA','HTML','CSS'],'num':0}
    return render(request,'home.html',data)

def services(request):
    return render(request,'services.html')