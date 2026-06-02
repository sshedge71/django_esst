from django.contrib import admin

from auth_app.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    list_filter = ('username',)
    search_fields = ('username',)
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password'),
        }),
    )
    