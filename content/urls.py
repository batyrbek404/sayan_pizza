from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet, NewsViewSet, AboutViewSet

router = DefaultRouter()
router.register(r'dishes', DishViewSet)
router.register(r'news', NewsViewSet)
router.register(r'about', AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
