from django.contrib import admin

from .models.book import Book, Publisher, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'registered')
    search_fields = ('title', 'author')
    list_filter = ('author', 'title')
    ordering = ('-author', '-title')

    list_per_page = 2
    # fields = ('title', 'author', 'published_date', 'registered')

# admin.site.register(Book, BookAdmin)
@admin.register(Publisher)
class BookInLine(admin.TabularInline):
    model = Book
    extra = 1
