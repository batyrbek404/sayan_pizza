from django.urls import path
from .views import TableBookingListAPIView, TableBookingDetailAPIView

urlpatterns = [
    path('', TableBookingListAPIView.as_view(), name='booking-list'),
    path('<int:pk>/', TableBookingDetailAPIView.as_view(), name='booking-detail'),
]
