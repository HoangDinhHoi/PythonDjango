from django.contrib import admin
from .models import PriceMenu
# Register your models here.


class PriceMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pub_date', 'pricemenu_image',)
    search_fields = ('name',)

    class Meta:
        model = PriceMenu
admin.site.register(PriceMenu, PriceMenuAdmin)
