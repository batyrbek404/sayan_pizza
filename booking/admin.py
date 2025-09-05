# menu/admin.py
from django.contrib import admin
from .models import TableBooking

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'email', 'phone')
