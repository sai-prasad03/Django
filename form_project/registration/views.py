from django.shortcuts import render
from . forms import StudentRegistrationForm


# Create your views here.

def showformdata(request):

    fm = StudentRegistrationForm()

    return render(request,'registration/studentform.html',{'form':fm})