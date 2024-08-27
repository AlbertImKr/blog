from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

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
            return redirect('login')
        return render(request, 'user/signup.html',
                      {'error': form.errors, 'form': form})
