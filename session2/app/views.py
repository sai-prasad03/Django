from django.shortcuts import render

# Create your views here.
def set_session(request):
    name = request.session['name']='saiprasad'
    request.session.set_expiry(600)
    return render(request, 'app/setsession.html')

def get_cookie(request):
    # keys = request.session.items()
    # return render(request,'app/getsession.html',{'keys':keys}) 
    name = request.session['name']
    return render(request,'app/getsession.html',{'name':name})

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'app/delsession.html')

