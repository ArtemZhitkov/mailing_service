from django import forms
from email_validator import validate_email, EmailNotValidError
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'area', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__()
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['area'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise forms.ValidationError(str(e))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number

class PasswordResetForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
        labels = {
            'password1': 'Новый пароль',
            'password2': 'Подтверждение нового пароля',
        }
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})