from django.contrib import admin

# Register your models here.
from src.apps.shipping.models import Shipping


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'details', 'residence', 'reception_date')
    search_fields = ('description', 'details', 'reception_date', 'residence__block', 'residence__number')
    list_filter = ('residence', )

    def get_queryset(self, request):
        qs = super(ShippingAdmin, self).get_queryset(request)
        return qs.order_by('residence', '-reception_date')
