from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404
from .models import MailMessage, Mailing, RecipientMail, MailingAttempt
from .forms import RecipientForm
from .services import MailingService


class RecipientMailListViews(ListView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_list.html'
    context_object_name = 'recipients'
    paginate_by = 10
    ordering = ['full_name']


class RecipientMailDetailViews(DetailView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_detail.html'
    context_object_name = 'recipient'


class RecipientMailCreateViews(CreateView):
    model = RecipientMail
    form_class = RecipientForm
    template_name = 'mailapp/recipient_mail_form.html'
    success_url = reverse_lazy('mailapp:recipient_list')


class RecipientMailUpdateViews(UpdateView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_form.html'
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailapp:recipient_detail')

    def get_success_url(self):
        recipient = self.object
        return reverse_lazy('mailapp:recipient_detail', kwargs={'pk': recipient.pk})


class RecipientMailDeleteViews(DeleteView):
    model = RecipientMail
    context_object_name = 'recipient'
    template_name = 'mailapp/recipient_mail_confirm_delete.html'
    success_url = reverse_lazy('mailapp:recipient_list')


class MailMessageListView(ListView):
    model = MailMessage
    template_name = 'mailapp/mail_message_list.html'
    context_object_name = 'messages'
    paginate_by = 10


class MailMessageCreateView(CreateView):
    model = MailMessage
    template_name = 'mailapp/mail_message_form.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailapp:mail_message_list')


class MailMessageUpdateView(UpdateView):
    model = MailMessage
    template_name = 'mailapp/mail_message_form.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailapp:mail_message_detail')

    def get_success_url(self):
        message = self.object
        return reverse_lazy('mailapp:mail_message_detail', kwargs={'pk': message.pk})


class MailMessageDetailView(DetailView):
    model = MailMessage
    template_name = 'mailapp/mail_message_detail.html'
    context_object_name = 'message'


class MailMessageDeleteView(DeleteView):
    model = MailMessage
    template_name = 'mail_message_confirm_delete.html'
    success_url = reverse_lazy('mailapp:mail_message_list')


class MailingCreateView(CreateView):
    model = Mailing
    template_name = 'mailapp/mailing_form.html'
    fields = ['message', 'recipients', 'frequency']
    success_url = reverse_lazy('mailapp:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailapp/mailing_detail.html'
    context_object_name = 'mailing'

    def post(self, request, *args, **kwargs):
        mailing = get_object_or_404(Mailing, pk=kwargs.get('pk'))
        MailingService.start_mailing(mailing)
        return redirect(reverse('mailapp:mailing_attempts'))



class MailingUpdateView(UpdateView):
    model = Mailing
    template_name = 'mailapp/mailing_form.html'
    fields = ['message', 'recipients']
    success_url = reverse_lazy('mailapp:mailing_detail')

    def get_success_url(self):
        mailing = self.object
        return reverse_lazy('mailapp:mailing_detail', kwargs={'pk': mailing.pk})


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailapp/mailing_list.html'
    context_object_name = 'mailings'
    paginate_by = 10


class MailingDeleteView(DeleteView):
    model = Mailing
    context_object_name = 'mailing'
    template_name = 'mailapp/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailapp:mailing_list')


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailapp/mailing_attempt_list.html'
    context_object_name = 'attempts'
    paginate_by = 10
