import secrets
from .models import User
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

class UserService:

    @staticmethod
    def send_verification_email(user):
        verification_token = secrets.token_urlsafe(16)
        user.verification_token = verification_token
        user.save()

        subject = 'Подтверждение аккаунта'
        message = f'Пожалуйста, перейдите по ссылке, чтобы подтвердить ваш аккаунт: http://localhost:8000/verify/{verification_token}'
        send_mail(subject, message, EMAIL_HOST_USER, [user.email])

    @staticmethod
    def reset_password(user):
        reset_token = secrets.token_urlsafe(16)
        user.reset_token = reset_token
        user.save()

        subject = 'Восстановление пароля'
        message = f'Пожалуйста, перейдите по ссылке, чтобы восстановить ваш пароль: http://localhost:8000/reset/{reset_token}'
        send_mail(subject, message, EMAIL_HOST_USER, [user.email])
