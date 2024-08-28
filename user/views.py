from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import UserSigninForm
from .forms import UserSignupForm


class SignupView(View):
    def get(self, request):
        form = UserSignupForm()
        return render(request, 'user/signup.html',
                      {'form': form})

    def post(self, request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'user/signup.html',
                      {'error': form.errors, 'form': form})


class SignInView(View):
    form_class = UserSigninForm
    template_name = 'user/signin.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                return render(request, self.template_name,
                              {'form': form,
                               'error': '이메일 또는 비밀번호가 일치하지 않습니다.'})
        return render(request, self.template_name,
                      {'form': form, 'error': form.errors})


class SignOutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')
