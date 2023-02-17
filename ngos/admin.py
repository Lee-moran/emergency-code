from django.contrib import admin
from .models import Category, NonGovernmentOrg


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'slug',
    )


class NonGovernmentOrgAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'friendly_name',
        'is_featured',
        'description',
        'website',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(NonGovernmentOrg, NonGovernmentOrgAdmin)
