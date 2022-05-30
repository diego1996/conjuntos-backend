from django.contrib import admin

# Register your models here.
from src.apps.residential.models import Residence, Block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(BlockAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'residence_type', 'block', 'number', 'phone', 'busy')
    search_fields = ('residence_type__name', 'block', 'number')
    list_filter = ('residence_type', 'block')

    def get_queryset(self, request):
        qs = super(ResidenceAdmin, self).get_queryset(request)
        return qs.order_by('block', 'number')
