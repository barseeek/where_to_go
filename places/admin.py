from django.contrib import admin
from places.models import TourCompany


@admin.register(TourCompany)
class TourCompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)