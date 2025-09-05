# menu/views.py
from rest_framework import viewsets
from .models import TableBooking
from .serializers import TableBookingSerializer

class TableBookingViewSet(viewsets.ModelViewSet):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
