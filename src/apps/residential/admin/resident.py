from django.contrib import admin

# Register your models here.
from src.apps.residential.models import Resident


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'resident_type', 'cellphone', 'whatsapp', 'residence', 'active')
    search_fields = (
        'first_name', 'last_name', 'resident_type', 'cellphone', 'whatsapp', 'residence__block', 'residence__number'
    )
    list_filter = ('resident_type', 'residence', 'active')

    def get_queryset(self, request):
        qs = super(ResidentAdmin, self).get_queryset(request)
        return qs.order_by('first_name', 'last_name')
