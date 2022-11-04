from django import forms

class RegistrarionForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 4:
            raise forms.ValidationError("name should be greter than 4 character")

        if len(valemail) < 6:
            raise forms.ValidationError("Email should be greter than 6 character")

