
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView
from django.urls import path

from users.apps import UserConfig
from users.views import RegisterView, ProfileView, UserPasswordResetConfirmView, \
    UserResetPasswordView, UserPasswordResetDoneView, success_registration, UsersListView

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('success_registration/', success_registration, name="success_registration"),
    path('view', UsersListView.as_view(), name="users_list"),

    path('reset_password/', UserResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_sent/', UserPasswordResetDoneView.as_view(), name='password_reset_don'),
    path('reset/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
