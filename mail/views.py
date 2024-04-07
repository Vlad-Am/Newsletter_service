import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog
from mail.forms import NewsletterForm, ClientForm, MessageForm, NewsletterModeratorForm
from mail.models import Newsletter, Client, Message, Logs
from mail.services import get_cache_for_mailings, get_cache_for_active_mailings


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        super().get_queryset()
        queryset = Client.objects.filter(owner=self.request.user)
        return queryset


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = ClientForm

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.owner = self.request.user
            new_client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('mail:client_list')
    form_class = ClientForm


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        super().get_queryset()
        queryset = Message.objects.filter(owner=self.request.user)
        return queryset


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = MessageForm

    def form_valid(self, form):
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.owner = self.request.user
            new_message.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mail:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    success_url = reverse_lazy('mail:message_list')
    form_class = MessageForm


class MailUpdateModeratorView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterModeratorForm
    success_url = reverse_lazy('mail:mail_list')
    permission_required = 'mail.set_is_activated'


class NewsletterListView(ListView):
    model = Newsletter

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = get_cache_for_mailings()
        context_data['active_mailings_count'] = get_cache_for_active_mailings()
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        context_data['clients_count'] = len(Client.objects.all())
        return context_data


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['clients'] = list(self.object.client.all())
        context_data['logs'] = list(Logs.objects.filter(newsletter=self.object))
        return context_data


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = NewsletterForm

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save(commit=False)
            new_mailing.owner = self.request.user
            new_mailing.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = NewsletterForm

    def get_success_url(self, *args, **kwargs):
        super().get_success_url()
        return reverse_lazy('mail:newsletter_detail', kwargs={'pk': self.object.pk})
