from django.contrib import admin
from .models import Product, Category, Designer


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'designer',
        'name',
        'category',
        'price',
        'image1',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DesignerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Designer, DesignerAdmin)
