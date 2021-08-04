from django.contrib import admin
from book.models import Book,Comment, Like

# Register your models here.


@admin.register(Book)
class BookApp(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Comment)
admin.site.register(Like)

