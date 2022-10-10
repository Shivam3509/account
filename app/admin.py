from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    class Meta():
        model = CustomUser
        list_display = ('email', 'is_active',)
        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Permissions', {'fields': ( 'is_active')}),
        )
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'is_active')}
            ),
        )
        search_fields = ('email',)
        ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)