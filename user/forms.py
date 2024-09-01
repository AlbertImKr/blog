from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User

from .models import Profile


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Email",
                "required": "True",
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "Id": "username",
                "placeholder": "Username",
                "required": "True",
                "aria-describedby": "usernameHelp",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "placeholder": "Password",
                "required": "True",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "confirm_password",
                "placeholder": "Confirm Password",
                "required": "True",
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("이메일이 이미 존재합니다.")
        return email


class UserSigninForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Username",
                "required": "True",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "placeholder": "Password",
                "required": "True",
            }
        )
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "job_title",
            "location",
            "bio",
            "birth_date",
            "email",
            "address",
            "facebook",
            "linkedin",
            "twitter",
            "tistory",
            "github",
            "website",
        )
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control',
                                                 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'tistory': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

