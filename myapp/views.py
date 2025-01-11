from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Restaurant, MenuItem, Review

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'myapp/restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'myapp/restaurant_detail.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = self.object.menu_items.all()
        context['reviews'] = self.object.reviews.all()
        return context
