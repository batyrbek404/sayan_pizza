from django.contrib import admin

from cart.models import Cart,CartItem

class CartItemInLine(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    inlines = (CartItemInLine,)

# Register your models here.
