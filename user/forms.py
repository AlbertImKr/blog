from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
                {'class': 'form-control', 'Id': 'username',
                 'placeholder': 'Username', 'required': 'True',
                 'aria-describedby': 'usernameHelp'})
        self.fields['email'].widget.attrs.update(
                {'class': 'form-control', 'id': 'email',
                 'placeholder': 'Email', 'required': 'True'})
        self.fields['password1'].widget.attrs.update(
                {'class': 'form-control', 'id': 'password',
                 'placeholder': 'Password', 'required': 'True'})
        self.fields['password2'].widget.attrs.update(
                {'class': 'form-control', 'id': 'confirm_password',
                 'placeholder': 'Confirm Password', 'required': 'True'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('이메일이 이미 존재합니다.')
        return email


class UserSigninForm(forms.Form):
    email = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={'class': 'form-control', 'id': 'email',
                           'placeholder': 'Email', 'required': 'True'}))

    password = forms.CharField(
            widget=forms.PasswordInput(
                    attrs={'class': 'form-control', 'id': 'password',
                           'placeholder': 'Password', 'required': 'True'}))
