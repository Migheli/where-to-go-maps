from django.contrib import admin
from .models import Place, Image



class ImagesInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class ClaimAdmin(admin.ModelAdmin):
    inlines = [
            ImagesInline,
        ]

@admin.register(Image)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['priority', 'title']

