from django.contrib import admin
from places.models import TourCompany, TourImage


class TourCompanyInline(admin.TabularInline):
    model = TourImage
    extra = 1


@admin.register(TourCompany)
class TourCompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TourCompanyInline]


@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    ordering = ('position',)
