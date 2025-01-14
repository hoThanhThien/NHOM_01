from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, Order, OrderDetail, User, Customer, LoyaltyCustomer, Promotion
from app_home.forms import UserForm, CustomUserChangeForm

# Register Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'size_ni', 'active')
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

# Register OrderDetail model
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    search_fields = ('order__id', 'product__name')

# Register User model
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = UserForm

    # Display fields in the list view
    list_display = ('id', 'username', 'email', 'role', 'phone', 'gender', 'birth_date', 'active')
    list_filter = ('role', 'active', 'gender')
    search_fields = ('username', 'email', 'phone')

    # Form for editing user details
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'phone', 'gender', 'birth_date', 'image', 'active', 'products'),
        }),
    )

    # Form for adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'phone', 'gender', 'birth_date', 'image', 'active'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

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