from django.shortcuts import render

# Create your views here.

def Fees_Django(request):

    return render(request,'fees/feesone.html',{'title':'Fees','cname':'Django Fees','Charge':3000})