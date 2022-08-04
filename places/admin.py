from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe


class ImagesInline(admin.TabularInline):
    model = Image

    fields = ('photo', 'get_preview_image', 'priority')

    readonly_fields = ['get_preview_image']
    list_display = ['priority', 'get_preview_image', 'title']

    def get_preview_image(self, obj):
        url = obj.photo.url
        width = '50'
        height = '200'
        return format_html('<img src="{}" width="{}" height={} />',
                           url,
                           'auto',
                           height
                           )

    get_preview_image.short_description = 'Предпросмотр'



@admin.register(Place)
class ClaimAdmin(admin.ModelAdmin):

    inlines = [
            ImagesInline,
        ]


@admin.register(Image)
class ClaimAdmin(admin.ModelAdmin):
    #readonly_fields = ['get_preview_image']
    list_display = ['priority', 'title']

