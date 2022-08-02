from django.contrib import admin
from .models import Place, Image

admin.site.register(Place)
# Register your models here.

@admin.register(Image)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['priority', 'title']
