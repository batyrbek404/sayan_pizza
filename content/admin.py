from django.contrib import admin
from .models import Dish, News, About  # <-- твои реальные модели

# Регистрируем модели в админке
admin.site.register(Dish)
admin.site.register(News)
admin.site.register(About)
