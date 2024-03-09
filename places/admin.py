from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from places.models import TourCompany, TourImage


class TourCompanyInline(SortableInlineAdminMixin, admin.TabularInline):
    model = TourImage
    extra = 1
    readonly_fields = ["tour_image",]
    fields = ('image', 'tour_image', 'position',)
    def tour_image(self, obj):
        return format_html(
            "<img src='{url}' width=200px>",
            url=obj.image.url)


@admin.register(TourCompany)
class TourCompanyAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TourCompanyInline,]


@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    ordering = ('position',)
