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

