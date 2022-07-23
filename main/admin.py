from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'count', 'published', 'is_shown', 'created')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('published', 'is_shown')
    list_filter = ('count', 'created')



admin.site.register(Book, BookAdmin)
