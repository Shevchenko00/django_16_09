from atexit import register

from django.contrib import admin

from .models.book import Book, Publisher, Author, Post


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'registered')
    search_fields = ('title', 'author')
    list_filter = ('author', 'title')
    ordering = ('-author', '-title')

    list_per_page = 2
    # fields = ('title', 'author', 'published_date', 'registered')



class BookInLine(admin.StackedInline):
    model = Book
    extra = 1


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInLine]
    list_display = ('name', 'registered_date')

admin.site.register(Author)
admin.site.register(Post)