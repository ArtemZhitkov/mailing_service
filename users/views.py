from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView
from .models import User
from .forms import UserRegisterForm, PasswordResetForm
from .services import UserService

class UsersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    permission_required = 'users.can_view_user_list'
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name ='users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        host = self.request.get_host()
        UserService.send_verification_email(user, host)
        return super().form_valid(form)

def email_verification(request, verification_token):
    user = get_object_or_404(User, verification_token=verification_token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


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