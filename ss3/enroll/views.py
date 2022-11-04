from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def user_info(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid:
            fm.save()
            messages.success(request,"your application has been created...")
    else:
            fm = StudentRegistration()
            
    return render(request,'enroll/register.html',{'form':fm})

    