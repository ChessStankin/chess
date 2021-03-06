from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Имя пользователя'
    )
    email = forms.EmailField(
        max_length=128,
        min_length=5,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Email'
    )
    password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
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
                'class': 'form-control'
            }
        ),
        label='Повторите пароль'
    )

    def passwords_equal(self):
        if self.cleaned_data['password'] == self.cleaned_data['password_confirm']:
            return True
        return False


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        max_length=128,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Имя пользователя / Email'
    )
    password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Пароль'
    )


class EmailForm(forms.Form):
    email = forms.EmailField(
        max_length=128,
        min_length=5,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Email'
    )


class PasswordEditForm(forms.Form):
    current_password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Текущий пароль'
    )
    new_password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Новый пароль'
    )
    new_password_confirm = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Повторите новый пароль'
    )

    def passwords_equal(self):
        if self.cleaned_data['new_password'] == self.cleaned_data['new_password_confirm']:
            return True
        return False

    def is_password_new(self):
        if self.cleaned_data['new_password'] != self.cleaned_data['current_password']:
            return True
        return False
