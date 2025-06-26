
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ContactsView(DetailView):
    model = Product
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')