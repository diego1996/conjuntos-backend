from django.contrib import admin

# Register your models here.
from src.apps.vehicles.models import VehicleType, VehicleColor, Vehicle


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(VehicleTypeAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(VehicleColor)
class VehicleColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(VehicleColorAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_type', 'vehicle_color', 'license_plate', 'residence')
    search_fields = (
        'vehicle_type__name', 'vehicle_color__name', 'license_plate', 'residence__block', 'residence__number'
    )
    list_filter = ('vehicle_type', 'vehicle_color', 'residence')

    def get_queryset(self, request):
        qs = super(VehicleAdmin, self).get_queryset(request)
        return qs.order_by('vehicle_type', 'license_plate')
