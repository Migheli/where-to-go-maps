from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase


class ImagesSortableInline(SortableTabularInline):

    model = Image
    fields = ['photo', 'get_preview_image']
    readonly_fields = ['get_preview_image']

    def get_preview_image(self, obj):
        url = obj.photo.url
        height = '200'
        return format_html(
            '<img src="{}" width="{}" height={} />',
            url,
            'auto',
            height
        )
    get_preview_image.short_description = 'Предпросмотр'


@admin.register(Place)
class ClaimAdmin(SortableAdminBase, admin.ModelAdmin):

    inlines = [
        ImagesSortableInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        'priority',
        'get_preview_image',
        'title'
    ]
    readonly_fields = ['get_preview_image']

    def get_preview_image(self, obj):
        url = obj.photo.url
        height = '200'
        return format_html(
            '<img src="{}" width="{}" height={} />',
            url,
            'auto',
            height
        )
    get_preview_image.short_description = 'Предпросмотр'


