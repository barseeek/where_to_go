from django.contrib import admin
from places.models import TourCompany, TourImage


@admin.register(TourCompany)
class TourCompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    pass