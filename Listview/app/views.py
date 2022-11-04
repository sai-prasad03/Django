from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from .models import Student
from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student

    # def get_queryset(request):# by using this method we can filter data
    #     return Student.objects.filter(course= 'python')

    # def get_context_data(self,*args, **kwargs):# this displays the list of objects
    #     context =  super().get_context_data(*args, **kwargs)
    #     context['Freshers'] = Student.objects.all().order_by('name')
    #     return context