from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404
from .models import MailMessage, Mailing, RecipientMail, MailingAttempt
from .forms import RecipientForm, MailingForm, MailMessageForm
from .services import MailingService

class IndexTemplateView(TemplateView):
    template_name = 'mailapp/index.html'
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_mailing'] = Mailing.objects.all().count()
        context['count_active_mailing'] = Mailing.objects.filter(status='Запущена').count()
        context['count_unique_recipients'] = RecipientMail.objects.all().count()
        return context



class RecipientMailListViews(LoginRequiredMixin, ListView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_list.html'
    context_object_name = 'recipients'
    paginate_by = 10
    ordering = ['full_name']


class RecipientMailDetailViews(LoginRequiredMixin, DetailView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_detail.html'
    context_object_name = 'recipient'


class RecipientMailCreateViews(LoginRequiredMixin, CreateView):
    model = RecipientMail
    form_class = RecipientForm
    template_name = 'mailapp/recipient_mail_form.html'
    success_url = reverse_lazy('mailapp:recipient_list')


class RecipientMailUpdateViews(LoginRequiredMixin, UpdateView):
    model = RecipientMail
    template_name = 'mailapp/recipient_mail_form.html'
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailapp:recipient_detail')

    def get_success_url(self):
        recipient = self.object
        return reverse_lazy('mailapp:recipient_detail', kwargs={'pk': recipient.pk})


class RecipientMailDeleteViews(LoginRequiredMixin, DeleteView):
    model = RecipientMail
    context_object_name = 'recipient'
    template_name = 'mailapp/recipient_mail_confirm_delete.html'
    success_url = reverse_lazy('mailapp:recipient_list')


class MailMessageListView(LoginRequiredMixin, ListView):
    model = MailMessage
    template_name = 'mailapp/mail_message_list.html'
    context_object_name = 'messages'
    paginate_by = 10


class MailMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailMessage
    template_name = 'mailapp/mail_message_form.html'
    form_class = MailMessageForm
    success_url = reverse_lazy('mailapp:mail_message_list')


class MailMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailMessage
    template_name = 'mailapp/mail_message_form.html'
    form_class = MailMessageForm
    success_url = reverse_lazy('mailapp:mail_message_detail')

    def get_success_url(self):
        message = self.object
        return reverse_lazy('mailapp:mail_message_detail', kwargs={'pk': message.pk})


class MailMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailMessage
    template_name = 'mailapp/mail_message_detail.html'
    context_object_name = 'message'


class MailMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailMessage
    template_name = 'mailapp/mail_message_confirm_delete.html'
    context_object_name = 'message'
    success_url = reverse_lazy('mailapp:mail_message_list')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    template_name = 'mailapp/mailing_form.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailapp:mailing_list')

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        return redirect(reverse('mailapp:mailing_list'))


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailapp/mailing_detail.html'
    context_object_name = 'mailing'

    def post(self, request, *args, **kwargs):
        mailing = get_object_or_404(Mailing, pk=kwargs.get('pk'))
        MailingService.start_mailing(mailing)
        return redirect(reverse('mailapp:mailing_attempts'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipients'] = RecipientMail.objects.filter(mailing=self.object)
        return context



class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    template_name = 'mailapp/mailing_form.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailapp:mailing_detail')

    def get_success_url(self):
        mailing = self.object
        return reverse_lazy('mailapp:mailing_detail', kwargs={'pk': mailing.pk})


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailapp/mailing_list.html'
    context_object_name = 'mailings'
    paginate_by = 10


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    context_object_name = 'mailing'
    template_name = 'mailapp/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailapp:mailing_list')


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'mailapp/mailing_attempt_list.html'
    context_object_name = 'attempts'
    paginate_by = 10
