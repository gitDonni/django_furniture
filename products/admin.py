from django.contrib import admin
from products.models import Categories, Products, ProductImage

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = ['name', 'category', 'slug', 'description', ('price', 'discount'), 'quantity']
    inlines = [ProductImageInline]



