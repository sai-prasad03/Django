import re
from django.shortcuts import render

from .models import Student

# Create your views here.
def student_info(request):
    stud = Student.objects.all()
    return render(request,'student/studentinfo.html',{'stu':stud})