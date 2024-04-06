from django.apps import AppConfig
from django.urls import path

from mail.apps import MailConfig
from mail.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterDeleteView, \
    NewsletterUpdateView, MessageListView, MessageDetailView, MessageUpdateView, MessageCreateView, MessageDeleteView, \
    ClientListView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView

app_name = MailConfig.name


urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('view/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_confirm_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('message_view/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_view/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_confirm_delete'),

]
