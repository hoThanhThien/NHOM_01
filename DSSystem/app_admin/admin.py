from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser
from .models import Product, Category, Order, User
from app_home.forms import UserForm, ProductForm, OrderForm, OrderDetailForm, CustomerForm, LoyaltyCustomerForm, PromotionForm

# Register Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'active')
    list_filter = ('category',)
    search_fields = ('name', 'diamond_origin')

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

# Register Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'ship_date')
    search_fields = ('order_date',)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User

    # Hiển thị các trường trong danh sách
    list_display = ('id', 'username', 'email', 'role', 'phone', 'gender', 'birth_date', 'active')
    list_filter = ('role', 'active', 'gender')
    search_fields = ('username', 'email', 'phone')

    # Form chỉnh sửa chi tiết người dùng
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'phone', 'gender', 'birth_date', 'image', 'active', 'products'),
        }),
    )

    # Form thêm người dùng mới
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'phone', 'gender', 'birth_date', 'image', 'active'),
        }),
    )

# Đăng ký User model với CustomUserAdmin
admin.site.register(User, CustomUserAdmin)