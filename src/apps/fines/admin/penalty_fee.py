from django.contrib import admin

# Register your models here.
from src.apps.fines.models import PenaltyFee, PenaltyFeeType


@admin.register(PenaltyFeeType)
class PenaltyFeeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(PenaltyFeeTypeAdmin, self).get_queryset(request)
        return qs.order_by('name')


@admin.register(PenaltyFee)
class PenaltyFeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'penalty_fee_type', 'penalty_fee_date', 'amount_to_paid', 'active', 'residence')
    search_fields = ('penalty_fee_type__name', 'description', 'residence__block', 'residence__number')
    list_filter = ('penalty_fee_type', 'residence', 'active')

    def get_queryset(self, request):
        qs = super(PenaltyFeeAdmin, self).get_queryset(request)
        return qs.order_by('residence', '-penalty_fee_date')
