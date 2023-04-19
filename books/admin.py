from django.contrib import admin
from .models import Author, Genre, Book, Review, Favorite

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'pub_date', 'average_rating', 'created_at', 'updated_at')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'text', 'created_at', 'updated_at')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)