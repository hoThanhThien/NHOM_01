from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Order # Import các model cần đăng ký

# Đăng ký Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'active')  # Hiển thị các cột
    list_filter = ('category',)  # Bộ lọc theo category
    search_fields = ('name', 'diamond_origin')  # Thêm chức năng tìm kiếm

# Đăng ký Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'ship_date')
    search_fields = ('order_date',)
    
