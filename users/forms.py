from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User

from mail.forms import StyleFormMixin


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserModeratorForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('is_active',)
