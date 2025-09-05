# menu/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableBookingViewSet

router = DefaultRouter()
router.register(r'bookings', TableBookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
