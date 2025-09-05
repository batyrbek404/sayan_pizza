from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100) #имя
    price = models.FloatField() # цена
    weight = models.FloatField() #масса
    composition = models.TextField() #состав
    image = models.ImageField(upload_to='dish_images') #фото
    is_available = models.BooleanField(default=True) #
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #категория

    def __str__(self):
        return self.name



class Review(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews',verbose_name='Блюдо')
    name = models.CharField(max_length=100,verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    rating = models.IntegerField(default=5,verbose_name='Рейтинг')
    comment = models.TextField(verbose_name='Комментарий')
    is_moderated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.dish.name} {self.name}'


