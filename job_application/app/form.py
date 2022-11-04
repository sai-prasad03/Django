from django import forms

class JobApplicationform(forms.Form):
    first_name = froms.CharField(max_length = 100)
    last_name = froms.CharField(max_length = 100)
    email = froms.EmailField(max_length = 100)
    job_role = froms.CharField(max_length = 50)
    address = froms.CharField(max_length = 120)
    city = froms.CharField(max_length = 40)
    pincode = froms.IntegerField()
    date = froms.DateField()
    file = froms.FileField()

