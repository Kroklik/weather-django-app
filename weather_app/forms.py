from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms

from weather_app.utils import send_email_for_verify

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='E-mail')
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Пароль'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Подтверждение пароля'
    )

    class Meta:
        model = User
        fields = ('email',)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(max_length=250, label='E-mail')
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Пароль'
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)

            if self.user_cache is None:
                raise self.get_invalid_login_error()

            if not self.user_cache.email_verified:
                raise ValidationError(
                    'E-mail не подтвержден. Проверьте почту',
                    code='invalid email'
                )

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
