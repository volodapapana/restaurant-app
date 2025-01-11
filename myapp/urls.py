from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
] 