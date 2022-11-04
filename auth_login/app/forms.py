from cProfile import label
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UserEditPRofileForm(UserChangeForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','is_active','password']
        label = {'email':'Email'}
