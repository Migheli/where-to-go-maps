from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe


class ImagesInline(admin.TabularInline):
    model = Image

    fields = ('photo', 'preview_image', 'priority')

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        url = obj.url
        width = '50'
        height = '50'
        # string = f'<img src="{url}" width="{width}" height={height} />'
        # print(f'СТРИНГ ---> {string}')
        return format_html("{} <b>{}</b> {}", mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=url,
                width=width,
                height=height,
            )
        )
                           )


    preview_image.short_description = 'Предпросмотр'



@admin.register(Place)
class ClaimAdmin(admin.ModelAdmin):

    inlines = [
            ImagesInline,
        ]

@admin.register(Image)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['priority', 'preview_image', 'title']

    def preview_image(self, obj):
        url = obj.photo.url
        width = '50'
        height = '50'
        # string = f'<img src="{url}" width="{width}" height={height} />'
        # print(f'СТРИНГ ---> {string}')
        return format_html("{} <b>{}</b> {}", mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=url,
                width=width,
                height=height,
            )
        )
                           )

    preview_image.short_description = 'Предпросмотр'

