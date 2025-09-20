from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_price = models.DecimalField(max_digits=8, decimal_places=2, default=200)

    # Новые поля для доставки
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # номер телефона
    delivery_address = models.TextField(blank=True, null=True)  # адрес доставки

    def __str__(self):
        return f'Корзина {self.pk} пользователя {self.user.username}'

    def items_total(self):
        """Стоимость всех блюд без доставки"""
        return sum(item.total_price() for item in self.items.all())

    def total_price(self):
        """Итоговая сумма с доставкой"""
        return self.items_total() + self.delivery_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.dish.name}'

    def total_price(self):
        return (self.dish.price or 0) * self.quantity
