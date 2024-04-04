from django.apps import AppConfig
from django.urls import path

from mail.apps import MailConfig
from mail.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterDeleteView, \
    NewsletterUpdateView

app_name = MailConfig.name


urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('view/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_confirm_delete'),
]
