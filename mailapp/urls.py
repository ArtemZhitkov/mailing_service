from django.urls import path
from . import views
from mailapp.apps import MailappConfig

app_name = MailappConfig.name

urlpatterns = [
    path('', views.RecipientMailListViews.as_view(), name='recipient_list'),
    path('create/', views.RecipientMailCreateViews.as_view(), name='recipient_create'),
    path('recipient_detail/<int:pk>/', views.RecipientMailDetailViews.as_view(), name='recipient_detail'),
    path('recipient_update/<int:pk>/', views.RecipientMailUpdateViews.as_view(), name='recipient_update'),
    path('recipient_delete/<int:pk>/', views.RecipientMailDeleteViews.as_view(), name='recipient_delete'),
    ]