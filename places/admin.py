from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import TourCompany, TourImage


MAX_WIDTH = 200
MAX_HEIGHT = 200


class TourCompanyInline(SortableInlineAdminMixin, admin.TabularInline):
    model = TourImage
    extra = 1
    readonly_fields = ['get_image_tag', ]
    fields = ('image', 'get_image_tag', 'position',)

    def get_image_tag(self, obj):
        return format_html(
            "<img src='{url}' style='max-width: {MAX_WIDTH}px; max-height: {MAX_HEIGHT}px;'>",
            url=obj.image.url,
            MAX_WIDTH=MAX_WIDTH,
            MAX_HEIGHT=MAX_HEIGHT
        )


@admin.register(TourCompany)
class TourCompanyAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TourCompanyInline, ]
    search_fields = ('title',)


@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    ordering = ('position',)
    autocomplete_fields = ('tour_company',)
