# from http.client import HTTPResponse
# import imp

import re
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def learn_Django(request):

#     return HttpResponse('Hello Django')

# def learn_python(request):

#     return HttpResponse('hello Python')
# from datetime import datetime

# def learn_Django(request):

#     return render(request,'courseone.html',{'nm':'Django', 'st':10})

# def learn_python(request):

#     cname = 'Python'
#     Duration = '3 Months'
#     seats = 50
#     python_details = {'nm':cname,'du':Duration,'st':seats}
#     return render(request,'coursetwo.html',python_details) 

# def Date_time(request):
    
#     d = datetime.now()

#     return render(request,'time.html',{'dt': d})

# def Names(request):

#     student = {'names':['saiprasad','akshay','samarth','prathamesh']}

#     return render(request,'courseone.html',student)

def learn_Django(request):

    return render(request,'course/info.html',{'nm':'Django Course'})