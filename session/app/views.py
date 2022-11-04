from django.shortcuts import render

# Create your views here.

def set_session(request):
    request.session['name']='saiprasad'
    return render(request, 'app/setsession.html')

def get_session(request):
    # name = request.session['name']
    name = request.session.get('name')
    return render(request, 'app/getsession.html',{'name':name})


def del_session(request):
    if 'name' in request.session:
        del request.session['name']
        return render(request, 'app/delsession.html')