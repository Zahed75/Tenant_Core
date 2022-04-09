from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(TenantDashboard)
class TenantDashboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'types_of_bill', 'bill')


@admin.register(ApartmentInfo)
class ApartmentInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat_no', 'date')


admin.site.register(User_Message)

admin.site.register(admin_dashboard)

admin.site.register(Parking_Fees)
