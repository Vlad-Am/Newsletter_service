from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail.forms import NewsletterForm
from mail.models import Newsletter


class NewsletterListView(ListView):
    model = Newsletter

    # def get_context_data(self, *args, **kwargs):
    #     """Получает данные о версиях экземпляра класса и выбирает текущую (активную) версию для продукта"""
    #     context = super().get_context_data(*args, **kwargs)
    #     products = self.get_queryset()
    #     for product in products:
    #         product.version = product.version_set.filter(working=True).first()
    #     context["object_list"] = products
    #
    #     return context


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = NewsletterForm

    def from_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')
    form_class = NewsletterForm

    def get_success_url(self, *args, **kwargs):
        super().get_success_url()
        return reverse_lazy('mail:newsletter_detail', kwargs={'pk': self.object.pk})
