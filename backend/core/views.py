from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Restaurant, FoodItem, Cart, CartItem, Order
from .serializers import *

# ── AUTH ──────────────────────────────────────

@api_view(['POST'])
def register(request):
    data = request.data
    if User.objects.filter(email=data['email']).exists():
        return Response({'error': 'Email already exists'}, status=400)
    user = User.objects.create(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone', ''),
        password_hash=make_password(data['password'])
    )
    return Response({'message': 'User created', 'user_id': user.id}, status=201)

@api_view(['POST'])
def login(request):
    data = request.data
    try:
        user = User.objects.get(email=data['email'])
        if check_password(data['password'], user.password_hash):
            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'name': user.name,
                'email': user.email
            })
        return Response({'error': 'Wrong password'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

# ── RESTAURANTS ───────────────────────────────

@api_view(['GET'])
def get_restaurants(request):
    restaurants = Restaurant.objects.filter(availability_status='open')
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_menu(request, restaurant_id):
    items = FoodItem.objects.filter(restaurant_id=restaurant_id, is_available=True)
    serializer = FoodItemSerializer(items, many=True)
    return Response(serializer.data)

# ── CART ──────────────────────────────────────

@api_view(['GET'])
def get_cart(request, user_id):
    cart, _ = Cart.objects.get_or_create(user_id=user_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    data = request.data
    cart, _ = Cart.objects.get_or_create(user_id=data['user_id'])
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        food_item_id=data['food_item_id'],
        defaults={'quantity': 1, 'price_at_addition': data['price']}
    )
    if not created:
        item.quantity += 1
        item.save()
    return Response({'message': 'Item added to cart'})

# ── ORDERS ────────────────────────────────────

@api_view(['POST'])
def place_order(request):
    data = request.data
    order = Order.objects.create(
        user_id=data['user_id'],
        restaurant_id=data['restaurant_id'],
        total_price=data['total_price'],
        delivery_address=data.get('delivery_address', ''),
        order_status='pending'
    )
    return Response({'message': 'Order placed', 'order_id': order.id}, status=201)

@api_view(['GET'])
def get_orders(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)