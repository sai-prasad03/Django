
from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)   # saved in database

            reg.save()
            # fm=Student()
    else:
        fm=StudentRegistration()
    stu=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stu})



# delete record
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return redirect('/')


# edit record

def update_data(request,id):
    if request.method=='POST':
        pi= User.objects.get(pk=id)
        fm1=StudentRegistration(request.POST,instance=pi)
        if fm1.is_valid():
           fm1.save()
           return redirect('/')
    # else:
    #        pi= User.objects.get(pk=id)
    #        fm=Student(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form1':fm1})
