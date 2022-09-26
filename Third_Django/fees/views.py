from django.shortcuts import render

# Create your views here.

def fees_Django(request):

    return render(request,'fees/feesone.html',{'title':'FEES','cname':'Django Fees','charge':3000})