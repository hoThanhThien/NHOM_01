from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.utils.html import format_html
from .models import OrderItem, Product, Category, Order,  User, Customer, LoyaltyCustomer, Promotion
from app_admin.models import User, Group
from app_home.forms import CustomUserCreationForm, CustomUserChangeForm
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'size_ni', 'active', 'image_tag')
    list_filter = ('category',)
    search_fields = ('name', 'diamond_origin')

    def image_tag(self, obj):
        
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return 'No Image'
    image_tag.short_description = 'Image'

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

# Register Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'ship_date',  'complete')
    search_fields = ('customer__username', 'transaction_id')
    list_filter = ('complete', 'ship_date')
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'date_added')
    search_fields = ('order__id', 'product__name')
    list_filter = ('date_added',)
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    filter_horizontal = ('user_permissions', 'groups')
    list_display = (
        'id', 'username', 'email', 'role', 'phone', 'gender', 'birth_date', 'image_tag', 'is_active', 'is_staff'
    )
    list_filter = ('role', 'is_active', 'gender')
    search_fields = ('username', 'email', 'phone')
    ordering = ('email',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Profile Image'

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Personal Info', {'fields': ('phone', 'role', 'gender', 'birth_date', 'image')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    readonly_fields = ('id',)  # Đặt ID chỉ đọc để tránh chỉnh sửa nhầm
    
    
# Register Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

# Register LoyaltyCustomer model
@admin.register(LoyaltyCustomer)
class LoyaltyCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'eligible_date', 'points_required', 'promotion')
    search_fields = ('customer__user__username',)

# Register Promotion model
@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('discount', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('discount',)
