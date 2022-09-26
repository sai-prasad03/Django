from django.shortcuts import render

# Create your views here.

def Home(request):

    return render(request,'course/home.html')

def About(request):

    return render(request,'course/About.html')

def Django(request):

    return render(request,'course/course.html')