from django.contrib import admin
from .models import StyleImage
# Register your models here.


class StyleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date', 'image')
    search_fields = ('title',)

    class Meta:
        model = StyleImage


admin.site.register(StyleImage, StyleAdmin)
