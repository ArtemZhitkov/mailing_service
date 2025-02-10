from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import MailMessage, Mailing, RecipientMail

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
    template_name = 'mailapp/recipient_mail_form.html'
    fields = ['email', 'full_name', 'comment']
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
    template_name = 'recipient_mail_delete.html'
    success_url = reverse_lazy('mailapp:recipient_mail_list')


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
    fields = ['message', 'recipients']
    success_url = reverse_lazy('mailapp:mailing_list')



class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailapp/mailing_detail.html'
    context_object_name = 'mailing'



class MailingListView(ListView):
    model = Mailing
    template_name = 'mailapp/mailing_list.html'
    context_object_name = 'mailings'
    paginate_by = 10
