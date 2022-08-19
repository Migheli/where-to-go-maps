from django.contrib import admin
from .models import Place, Image
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase
from places.mixin_classes import ImagePreviewMixin


class ImagesSortableInline(SortableTabularInline, ImagePreviewMixin):

    model = Image
    fields = ['photo', 'get_preview_image']
    readonly_fields = ['get_preview_image']


@admin.register(Place)
class ClaimAdmin(SortableAdminBase, admin.ModelAdmin):

    inlines = [
        ImagesSortableInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin, ImagePreviewMixin):
    list_display = [
        'priority',
        'get_preview_image',
    ]
    readonly_fields = ['get_preview_image']
