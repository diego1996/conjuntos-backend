from django.contrib import admin

# Register your models here.
from src.apps.bookings.models import BookingSpace, Booking


@admin.register(BookingSpace)
class BookingSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(BookingSpaceAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_space', 'start_date', 'end_date', 'residence')
    search_fields = ('booking_space__name', 'residence__block', 'residence__number')
    list_filter = ('booking_space', 'residence')

    def get_queryset(self, request):
        qs = super(BookingAdmin, self).get_queryset(request)
        return qs.order_by('-start_date')
