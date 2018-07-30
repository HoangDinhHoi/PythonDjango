from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'date','book_time', 'email',)
    search_fields = ('name',)
    class Meta:
        model = Book           
admin.site.register(Book, BookAdmin)
