from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин'
            }
        ),
        label='Логин'
    )
    email = forms.CharField(
        max_length=128,
        min_length=5,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail'
            }
        ),
        label='E-mail'
    )
    password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        ),
        label='Пароль'
    )
    password_confirm = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль'
            }
        ),
        label='Повторите пароль'
    )

    def passwords_equal(self):
        if self.cleaned_data['password'] == self.cleaned_data['password_confirm']:
            return True
        return False


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин',
            }
        ),
        label='Логин'
    )
    password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль',
            }
        ),
        label='Пароль'
    )