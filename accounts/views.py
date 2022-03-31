from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms import UserCreationForm
from accounts.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView


class Login(LoginView):
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("shop:index")
        return super().dispatch(request, *args, **kwargs)


class Register(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("shop:index")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:login')


class ResetPass(PasswordResetView):
    template_name = 'accounts/password/reset.html'
    success_url = reverse_lazy('accounts:resetdone')
    email_template_name = 'accounts/password/password_reset_email.html'


class ResetPassDone(PasswordResetDoneView):
    template_name = 'accounts/password/password_reset_done.html'


class RestPassConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:resetdonecomplete')


class RestPassComplate(PasswordResetCompleteView):
    template_name = 'accounts/password/password_reset_complate.html'
