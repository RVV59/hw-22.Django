from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Product



class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'