from django.contrib import admin
from .models import (
    User, Restaurant, RestaurantOwner, FoodItem,
    Order, OrderItem, Payment, Delivery,
    Cart, CartItem, DeliveryRider, Review, 
    PromoCode, Address, Admin
)

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(RestaurantOwner)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(DeliveryRider)
admin.site.register(Review)
admin.site.register(PromoCode)
admin.site.register(Address)