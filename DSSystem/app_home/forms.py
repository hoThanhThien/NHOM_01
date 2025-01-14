from django import forms
from app_admin.models import User, Product, Order, OrderDetail, Customer, LoyaltyCustomer, Promotion


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'gender', 'birth_date', 'role', 'image', 'is_active']  # Include other fields as needed
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'carat_weight', 'diamond_origin', 'price', 'provider_id', 'quantity', 'image', 'active']
        widgets = {
            'image': forms.ClearableFileInput(),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user']


class LoyaltyCustomerForm(forms.ModelForm):
    class Meta:
        model = LoyaltyCustomer
        fields = ['customer', 'eligible_date', 'points_required', 'promotion']
        widgets = {
            'eligible_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['discount', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'ship_date', 'status']
        widgets = {
            'ship_date': forms.DateInput(attrs={'type': 'date'}),
        }


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order', 'product', 'quantity']
