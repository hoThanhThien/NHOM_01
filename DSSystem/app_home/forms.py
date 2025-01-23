from django import forms
from app_admin.models import User, Product, Order, OrderDetail, Customer, LoyaltyCustomer, Promotion

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app_admin.models import User

class CustomUserCreationForm(UserCreationForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'gender', 'birth_date', 'image', 'is_active']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
   



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'category', 'carat_weight', 'size_ni', 'diamond_origin', 'price', 'provider', 'quantity', 'image', 'active']
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