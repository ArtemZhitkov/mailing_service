from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateView, email_verification, reset_password, UserProfileUpdateView, UserProfileDetailView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='mailapp:mailing_list'), name='logout'),
    path('verify/<str:token>/', email_verification, name='verify_email'),
    path('reset/<str:token>', reset_password, name='reset_password'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/<int:pk>/', UserProfileUpdateView.as_view(), name='edit_profile')
]
