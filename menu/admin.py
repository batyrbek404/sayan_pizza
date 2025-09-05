from django.contrib import admin
from menu.models import Dish
from .models import Dish, Category,Review


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass