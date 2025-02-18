from django import forms
from app_admin.models import OrderItem, User, Product, Order,Customer, LoyaltyCustomer, Promotion

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
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'gender', 'birth_date', 'image', 'active']
        widgets = {
            'password': forms.PasswordInput(),
            'image': forms.ClearableFileInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
       # user.set_password(self.cleaned_data['password'])  # Mã hóa mật khẩu
        if commit:
            user.save()
        return user
   



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'carat_weight', 'size_ni', 'diamond_origin', 'price', 'provider', 'quantity', 'image', 'active', 'description']
        widgets = {
            'image': forms.ClearableFileInput(),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'point']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'point': forms.NumberInput(attrs={'class': 'form-control'}),
        }

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
        fields = ['customer', 'ship_date', 'address', 'complete']
        widgets = {
            'ship_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']
        widgets = {
            'order': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than 0.")
        if product and quantity > product.quantity:
            raise forms.ValidationError("Not enough stock available.")
        return quantity