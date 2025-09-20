from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import CartItem, Cart
from menu.models import Dish
from .serializers import CartSerializer, CartItemSerializer


# Получение корзины
class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        # пересчитываем delivery_price автоматически
        if cart.items_total() > 2000:
            cart.delivery_price = 0
        else:
            cart.delivery_price = 200
        cart.save()
        return cart


# Добавление блюда в корзину
class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        dish = serializer.validated_data['dish']
        quantity = serializer.validated_data['quantity']

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            dish=dish,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()
        serializer.instance = item

        # пересчёт доставки
        if cart.items_total() > 2000:
            cart.delivery_price = 0
        else:
            cart.delivery_price = 200
        cart.save()


# Удаление блюда из корзины
class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CartItem.objects.all()

    def delete(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        item_id = kwargs['pk']
        try:
            item = CartItem.objects.get(pk=item_id, cart=cart)
            item.delete()

            # пересчёт доставки
            if cart.items_total() > 2000:
                cart.delivery_price = 0
            else:
                cart.delivery_price = 200
            cart.save()

            return Response({'detail': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


# Обновление данных корзины (телефон, адрес)
class UpdateCartView(generics.UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart
