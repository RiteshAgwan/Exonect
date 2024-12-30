from django.contrib import admin
from .models import Product, Category, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    inlines = [ReviewInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)