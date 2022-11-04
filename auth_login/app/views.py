from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,UserEditPRofileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
#Sign_up view function

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Your application Created Succesfully..!!!")
    else:
        fm = SignupForm()

    return render(request, 'app/signup.html', {'form':fm})

#login View function

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data =request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()

        return render(request, 'app/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


# profile view function

def profile(request):
    if request.user.is_authenticated:
        fm = UserEditPRofileForm(instance=request.user)
        return render(request, 'app/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def old_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Your password has been changed successfully")
                return HttpResponseRedirect('/profile/')
                
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request, 'app/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')