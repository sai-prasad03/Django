from pipes import Template
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from django.views.generic.detail import DetailView

# Create your views here.

class StudentCreateviewForm(CreateView):
    model = Student
    fields = ['name','email','password']
    template_name = 'app/student.html'
    success_url =  '/thanks/'

class ThanksformSubmitted(TemplateView):
    template_name = 'app/thanks.html'

class UpdateStudentView(UpdateView):
    model = Student
    fields = ['name','email','password']

class StudentDetailView(DetailView):
    model = Student

class StudentDeleteView(DeleteView):
    model = Student
    success_url= '/create/'