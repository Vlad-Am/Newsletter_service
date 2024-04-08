import secrets
import time

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.views import (PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from config import settings
from users.forms import (UserModeratorForm, UserProfileForm,
                         UserRegistrationForm)
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/register.html"
    success_url = reverse_lazy("users:success_registration")

    def form_valid(self, form):
        token = secrets.token_hex(16)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f"http://{host}/users/activate/{token}"
        message = f"""Для активации вашего аккаунта перейдите по ссылке:
                {link}"""
        time.sleep(2)
        send_mail(
            "Верификация почты",
            message,
            settings.EMAIL_HOST_USER,
            [
                user.email,
            ],
        )
        return super().form_valid(form)


def success_registration(request):
    return render(request, "user/success_registration.html")


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return render(request, "user/login.html", status=200)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")
    template_name = "user/user_form.html"

    def get_object(self, queryset=None):
        return self.request.user


class UsersListView(ListView):
    model = User
    template_name = "user/user_list.html"


# class ProfileUpdateModeratorView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = User
#     form_class = UserModeratorForm
#     success_url = reverse_lazy('mail:mail_list')
#     permission_required = 'user.set_is_activated'
#     template_name = 'user/user_form.html'


class UserResetPasswordView(PasswordResetView):
    """
    Стартовая страница сброса пароля почте
    """

    success_url = reverse_lazy("users:password_reset_don")
    template_name = "registration/password_reset_conf.html"
    email_template_name = "registration/password_reset_mail.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Представление установки нового пароля(страница на которую переходит пользователь для сброса пароля)
    """

    success_url = reverse_lazy("users:login")
    template_name = "registration/entering_new_password.html"


class UserPasswordResetDoneView(PasswordResetDoneView):
    """
    Представление успешной отправки сообщения на почту
    """

    template_name = "registration/successful_password_change.html"


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserModeratorForm
    permission_required = "users.set_is_activated"
    success_url = "users:users_list"
    template_name = "user/user_form.html"

    def get_success_url(self):
        return reverse("users:list_view")


@login_required
@permission_required(["users.view_user", "users.set_is_activated"])
def get_users_list(request):
    users_list = User.objects.all()
    context = {
        "object_list": users_list,
        "title": "Список пользователей сервиса",
    }
    return render(request, "user/user_list.html", context)
