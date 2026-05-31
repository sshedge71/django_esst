import csv
from datetime import timezone
from django.http import HttpResponse

from django.http import HttpResponse
from django.contrib import admin

# Register your models here.
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author', 'published_date')

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'birth_date', 'mobile', 'email')
#     search_fields = ('name', 'email')
#     list_filter = ('birth_date',)

# admin.site.register(Book, BookAdmin)

# admin.site.register(Author, list_display = ('name', 'birth_date', 'mobile', 'email'), 
#                     search_fields = ('name', 'email'), 
#                     list_filter = ('birth_date',))



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'mobile', 'email')
    search_fields = ('name', 'email')
    list_filter = ('birth_date',)
    
    fieldsets = (
    ('Personal Info', {
        'fields': ('name', 'birth_date')
    }),
    ('Contact Info', {
        'fields': ('mobile', 'email')
    }),
)   
    ordering = ('name',)
    readonly_fields = ('mobile',)
    list_per_page = 10
