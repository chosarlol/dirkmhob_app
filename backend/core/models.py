from django.db import models
from django.contrib.auth.models import AbstractBaseUser
 
 
# ─────────────────────────────────────────────
# ADMIN
# ─────────────────────────────────────────────
class Admin(models.Model):
    username       = models.CharField(max_length=50, unique=True)
    email          = models.CharField(max_length=100, unique=True)
    password_hash  = models.CharField(max_length=255)
    admin_role     = models.CharField(max_length=30)
    last_login     = models.DateTimeField(null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.username
 
    class Meta:
        db_table = "admin"
 
 
# ─────────────────────────────────────────────
# USER (Customer)
# ─────────────────────────────────────────────
class User(models.Model):
    name            = models.CharField(max_length=100)
    email           = models.CharField(max_length=150, unique=True)
    phone           = models.CharField(max_length=20, null=True, blank=True)
    password_hash   = models.CharField(max_length=255)
    date_joined     = models.DateTimeField(auto_now_add=True)
    user_status     = models.CharField(max_length=20, default="active")
    last_update     = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        db_table = "user"
 
 
# ─────────────────────────────────────────────
# ADDRESS
# ─────────────────────────────────────────────
class Address(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address_unit   = models.CharField(max_length=200, null=True, blank=True)
    address_street = models.CharField(max_length=200)
    city           = models.CharField(max_length=100)
    state          = models.CharField(max_length=100, null=True, blank=True)
    postal_code    = models.CharField(max_length=20, null=True, blank=True)
    latitude       = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude      = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    is_default     = models.BooleanField(default=False)
 
    def __str__(self):
        return f"{self.user.name} - {self.address_street}"
 
    class Meta:
        db_table = "address"
 
 
# ─────────────────────────────────────────────
# RESTAURANT OWNER
# ─────────────────────────────────────────────
class RestaurantOwner(models.Model):
    owner_name     = models.CharField(max_length=100)
    email          = models.CharField(max_length=100, unique=True)
    password_hash  = models.CharField(max_length=255)
    phone_number   = models.CharField(max_length=20, null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    last_update    = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.owner_name
 
    class Meta:
        db_table = "restaurant_owner"
 
 
# ─────────────────────────────────────────────
# RESTAURANT
# ─────────────────────────────────────────────
class Restaurant(models.Model):
    owner           = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE, related_name="restaurants")
    restaurant_name = models.CharField(max_length=150)
    description     = models.TextField(null=True, blank=True)
    phone_number    = models.CharField(max_length=20, null=True, blank=True)
    email           = models.CharField(max_length=100, null=True, blank=True)
    address         = models.CharField(max_length=255, null=True, blank=True)
    city            = models.CharField(max_length=100, null=True, blank=True)
    latitude        = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude       = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    rating          = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    availability_status = models.CharField(max_length=30, default="open")
    opening_time    = models.TimeField(null=True, blank=True)
    closing_time    = models.TimeField(null=True, blank=True)
    delivery_fee    = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    last_update     = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.restaurant_name
 
    class Meta:
        db_table = "restaurant"
 
 
# ─────────────────────────────────────────────
# FOOD ITEM (Menu)
# ─────────────────────────────────────────────
class FoodItem(models.Model):
    restaurant    = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="food_items")
    food_name     = models.CharField(max_length=150)
    description   = models.TextField(null=True, blank=True)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    category      = models.CharField(max_length=50, null=True, blank=True)
    image_url     = models.CharField(max_length=255, null=True, blank=True)
    is_vegetarian = models.BooleanField(default=False)
    is_available  = models.BooleanField(default=True)
    preparation_time = models.IntegerField(null=True, blank=True)  # in minutes
    last_update   = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"{self.food_name} ({self.restaurant.restaurant_name})"
 
    class Meta:
        db_table = "food_item"
 
 
# ─────────────────────────────────────────────
# PROMO CODE
# ─────────────────────────────────────────────
class PromoCode(models.Model):
    code               = models.CharField(max_length=50, unique=True)
    description        = models.CharField(max_length=255, null=True, blank=True)
    discount_type      = models.CharField(max_length=30)   # "percentage" or "fixed"
    discount_value     = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_amount   = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_discount       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valid_from         = models.DateField()
    valid_until        = models.DateField()
    usage_limit        = models.IntegerField(null=True, blank=True)
    times_used         = models.IntegerField(default=0)
    is_active          = models.BooleanField(default=True)
 
    def __str__(self):
        return self.code
 
    class Meta:
        db_table = "promo_code"
 
 
# ─────────────────────────────────────────────
# DELIVERY RIDER
# ─────────────────────────────────────────────
class DeliveryRider(models.Model):
    rider_name         = models.CharField(max_length=100)
    email              = models.CharField(max_length=100, unique=True)
    phone_number       = models.CharField(max_length=20, unique=True)
    password_hash      = models.CharField(max_length=255)
    vehicle_number     = models.CharField(max_length=50, null=True, blank=True)
    current_latitude   = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    current_longitude  = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    rider_status       = models.CharField(max_length=30, default="offline")
    # status options: offline, available, on_delivery
    rating             = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_deliveries   = models.IntegerField(default=0)
    last_update        = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.rider_name
 
    class Meta:
        db_table = "delivery_rider"
 
 
# ─────────────────────────────────────────────
# CART
# ─────────────────────────────────────────────
class Cart(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    restaurant     = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount   = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at     = models.DateTimeField(auto_now_add=True)
    last_update    = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Cart of {self.user.name}"
 
    class Meta:
        db_table = "cart"
 
 
# ─────────────────────────────────────────────
# CART ITEM
# ─────────────────────────────────────────────
class CartItem(models.Model):
    cart           = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    food_item      = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity       = models.IntegerField(default=1)
    price_at_addition = models.DecimalField(max_digits=10, decimal_places=2)
    added_at       = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.quantity}x {self.food_item.food_name}"
 
    class Meta:
        db_table = "cart_item"
 
 
# ─────────────────────────────────────────────
# ORDER
# ─────────────────────────────────────────────
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending",    "Pending"),
        ("confirmed",  "Confirmed"),
        ("preparing",  "Preparing"),
        ("picked_up",  "Picked Up"),
        ("delivered",  "Delivered"),
        ("cancelled",  "Cancelled"),
    ]
 
    user               = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    restaurant         = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rider              = models.ForeignKey(DeliveryRider, on_delete=models.SET_NULL, null=True, blank=True)
    promo_code         = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)
    address            = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    order_date         = models.DateTimeField(auto_now_add=True)
    order_status       = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")
    order_notes        = models.CharField(max_length=300, null=True, blank=True)
    subtotal           = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    delivery_fee       = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_amount    = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tax_amount         = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_price        = models.DecimalField(max_digits=10, decimal_places=2)
    special_instructions = models.TextField(null=True, blank=True)
    last_update        = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Order #{self.id} by {self.user.name}"
 
    class Meta:
        db_table = "order"
 
 
# ─────────────────────────────────────────────
# ORDER ITEM
# ─────────────────────────────────────────────
class OrderItem(models.Model):
    order          = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food_item      = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity       = models.IntegerField()
    unit_price     = models.DecimalField(max_digits=10, decimal_places=2)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2)
    special_requests = models.TextField(null=True, blank=True)
 
    def __str__(self):
        return f"{self.quantity}x {self.food_item.food_name} (Order #{self.order.id})"
 
    class Meta:
        db_table = "order_item"
 
 
# ─────────────────────────────────────────────
# PAYMENT
# ─────────────────────────────────────────────
class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending",  "Pending"),
        ("success",  "Success"),
        ("failed",   "Failed"),
        ("refunded", "Refunded"),
    ]
 
    order              = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    payment_method     = models.CharField(max_length=100)   # e.g. ABA, Wing, Cash
    amount             = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id     = models.CharField(max_length=100, null=True, blank=True)
    transaction_date   = models.DateTimeField(null=True, blank=True)
    status             = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")
    details            = models.TextField(null=True, blank=True)
    last_update        = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.status}"
 
    class Meta:
        db_table = "payment"
 
 
# ─────────────────────────────────────────────
# DELIVERY
# ─────────────────────────────────────────────
class Delivery(models.Model):
    STATUS_CHOICES = [
        ("assigned",   "Assigned"),
        ("picked_up",  "Picked Up"),
        ("delivered",  "Delivered"),
        ("failed",     "Failed"),
    ]
 
    order              = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="delivery")
    rider              = models.ForeignKey(DeliveryRider, on_delete=models.SET_NULL, null=True)
    assigned_at        = models.DateTimeField(null=True, blank=True)
    picked_up_at       = models.DateTimeField(null=True, blank=True)
    delivered_at       = models.DateTimeField(null=True, blank=True)
    delivery_status    = models.CharField(max_length=30, choices=STATUS_CHOICES, default="assigned")
    order_latitude     = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    order_longitude    = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    delivery_notes     = models.TextField(null=True, blank=True)
    last_update        = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
 
    class Meta:
        db_table = "delivery"
 
 
# ─────────────────────────────────────────────
# REVIEW
# ─────────────────────────────────────────────
class Review(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    restaurant     = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    rider          = models.ForeignKey(DeliveryRider, on_delete=models.SET_NULL, null=True, blank=True)
    order          = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating         = models.IntegerField()   # 1–5
    comment        = models.TextField(null=True, blank=True)
    review_date    = models.DateTimeField(auto_now_add=True)
    created_at     = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Review by {self.user.name} for {self.restaurant.restaurant_name}"
 
    class Meta:
        db_table = "review"