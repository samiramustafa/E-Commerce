from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category', )

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount', 'bestseller', 'category', 'subcategory')
    search_fields = ('title', 'description')
    list_filter = ('category', 'subcategory', 'bestseller')
    readonly_fields = ['created_at']
    inlines = [ProductImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

