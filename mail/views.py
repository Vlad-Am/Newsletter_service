from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail.forms import NewsletterForm, ClientForm, MessageForm
from mail.models import Newsletter, Client, Message


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


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


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter


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
