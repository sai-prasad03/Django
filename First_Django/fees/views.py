from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def fees_django(request):

#     return HttpResponse(30000)


# def fees_python(request):

#     return HttpResponse(40000)
    
# def fees_django(request):

#     return render(request,'feesone.html')


# def fees_python(request):

#     return render(request,'feestwo.html')
    

def fees_django(request):

    return render(request,'fees/info.html',{'nm':'Django Fees'})
