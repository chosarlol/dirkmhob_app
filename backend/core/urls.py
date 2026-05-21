from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('auth/register/', views.register),
    path('auth/login/',    views.login),

    # Restaurants
    path('restaurants/',              views.get_restaurants),
    path('restaurants/<int:restaurant_id>/menu/', views.get_menu),

    # Cart
    path('cart/<int:user_id>/',  views.get_cart),
    path('cart/add/',            views.add_to_cart),

    # Orders
    path('orders/place/',            views.place_order),
    path('orders/<int:user_id>/',    views.get_orders),
]