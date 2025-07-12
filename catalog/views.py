from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm


class ContactsView(TemplateView):
    template_name = 'contacts.html'

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publish_status='published')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_superuser


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.delete_product') or user.is_superuser


class ProductUnpublishView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Product
    # Мы не будем отображать шаблон, но DetailView требует его наличия
    template_name = 'product_detail.html'

    def test_func(self):
        return self.request.user.has_perm('catalog.can_unpublish_product') or self.request.user.is_superuser

    def get(self, request, *args, **kwargs):

        product = self.get_object()

        product.publish_status = 'draft'
        product.save()
        return redirect('catalog:home')
