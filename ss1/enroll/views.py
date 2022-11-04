from django.shortcuts import render, HttpResponseRedirect

from .form import RegistrarionForm
def thankyou(request):
    return render(request, 'success.html')

# Create your views here.
def ShowFormData(request):
    if request.method == 'POST':
        fm = RegistrarionForm(request.POST)
        if fm.is_valid():

            return HttpResponseRedirect('/reg/success')


    else:
        fm = RegistrarionForm()
        print('ye get request se aaya hai')

    return render(request, 'register.html', {"form": fm})
