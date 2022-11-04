from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

class Enroll(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'app/home.html',{'form':form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you Form Submitted..')
