from django.urls import path
from . import views
from mailapp.apps import MailappConfig

app_name = MailappConfig.name

urlpatterns = [
    path('', views.RecipientMailListViews.as_view(), name='recipient_list'),
    path('create/', views.RecipientMailCreateViews.as_view(), name='recipient_create'),
    path('recipient/detail/<int:pk>/', views.RecipientMailDetailViews.as_view(), name='recipient_detail'),
    path('recipient/update/<int:pk>/', views.RecipientMailUpdateViews.as_view(), name='recipient_update'),
    path('recipient/delete/<int:pk>/', views.RecipientMailDeleteViews.as_view(), name='recipient_delete'),
    path('message/create/', views.MailMessageCreateView.as_view(), name='create_message'),
    path('message/detail/<int:pk>/', views.MailMessageDetailView.as_view(), name='mail_message_detail'),
    path('message/update/<int:pk>/', views.MailMessageUpdateView.as_view(), name='mail_update_message'),
    path('message/delete/<int:pk>/', views.MailMessageDeleteView.as_view(), name='mail_delete_message'),
    path('message/list/', views.MailMessageListView.as_view(), name='mail_message_list'),
    ]