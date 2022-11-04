
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
#set cookie function

def setcookie(request):
    response = render(request,'setcookie.html')
    #response.set_cookie('name', 'saiprasad', max_age=60) cookie expires in 60 seconds
    response.set_cookie('name', 'saiprasad', expires= datetime.utcnow()+timedelta(days=2))
    # cookie will be expires after 2 days
    return response

#get cookie function

def get_cookie(request):
    #name = request.COOKIES['name']
    name = request.COOKIES.get('name')
    return render(request, 'getcookie.html',{'name':name})

#delete cookie Function

def del_cookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response