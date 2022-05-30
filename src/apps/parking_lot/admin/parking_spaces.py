from django.contrib import admin

# Register your models here.
from src.apps.parking_lot.models import ParkingZone, ParkingSpace


@admin.register(ParkingZone)
class ParkingZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(ParkingZoneAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_zone', 'number', 'parking_space_type', 'residence')
    search_fields = ('parking_zone__name', 'parking_space_type__name', 'residence__block', 'residence__number')
    list_filter = ('parking_zone', 'parking_space_type', 'residence')

    def get_queryset(self, request):
        qs = super(ParkingSpaceAdmin, self).get_queryset(request)
        return qs.order_by('parking_zone', 'number')
