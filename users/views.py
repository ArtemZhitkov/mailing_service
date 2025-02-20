from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import User
from .forms import UserRegisterForm, PasswordResetForm
from .services import UserService


class UserCreateView(CreateView):
    template_name ='users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('mailapp:mailing_list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        UserService.send_verification_email(user)
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))

def reset_password(request, token):
    user = get_object_or_404(User, token=token)
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('users:login'))
    else:
        form = PasswordResetForm()
    return render(request, 'users/reset_password.html', {'form': form})


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/profile_edit.html'
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('users:profile_detail')
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('users:profile_detail', kwargs={'pk': self.kwargs['pk']})

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile_detail.html'
    login_url = reverse_lazy("users:login")
    context_object_name = 'user'