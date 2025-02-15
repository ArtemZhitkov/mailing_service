from .models import Mailing, MailingAttempt, MailMessage
from django.utils import timezone
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER



class MailingService:
    @staticmethod
    def start_mailing(mailing):
        mailing.start_time = timezone.now()
        mailing.status = "Запущена"
        mailing.save()

        subject = mailing.message.subject
        message = mailing.message.body
        recipients = [recipient.email for recipient in mailing.recipients.all()]
        for recipient in recipients:
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [recipient,]
            )

            if send_mail:
                mailing_attempt = MailingAttempt.objects.create(
                    status = MailingAttempt.SUCCESSFULLY,
                    mailing = mailing
                )
                mailing_attempt.save()
            else:
                mailing_attempt = MailingAttempt.objects.create(
                    status = MailingAttempt.UNSUCCESSFULLY,
                    mail_server_response = send_mail,
                    mailing = mailing
                )
                mailing_attempt.save()




