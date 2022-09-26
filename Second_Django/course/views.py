from django.shortcuts import render

# Create your views here.

def learn_Django(request):

    return render(request,'course/courseone.html',{'title':'Django','cname':'Django Course'})