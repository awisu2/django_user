from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'username',
        })
    )
    password = forms.CharField(
        label='password',
        min_length=1,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': '********',
        })
    )

    next = forms.CharField(
        label='next',
        max_length=255,
        required=False,
        widget=forms.HiddenInput()
    )
