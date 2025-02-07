import json
from queue import Full
from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from app_admin.models import Product, User, Category, Order, OrderItem
from .forms import ProductForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.template import loader
# Home Page
def home(request):
    return render(request, 'home.html')
def app_home(request):
     products = Product.objects.all()
     return render(request, 'app_home/app/home.html', {'products': products})
def app_shopHome(request):
     products = Product.objects.all()
     return render(request, 'app_home/app/shopHome.html', {'products': products})
def logoutPage(request):
    logout(request)
    return redirect('login')

from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Chuyển hướng nếu đã đăng nhập

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Kiểm tra username rỗng hoặc password rỗng
        if not username or not password:
            messages.error(request, "Please fill in both username and password fields.")
        else:
            User = get_user_model()
            try:
                user = User.objects.get(username=username)
                
                # So sánh mật khẩu trực tiếp 
                if user.password == password:
                    login(request, user)
                    return redirect('home')  # Chuyển hướng về trang chủ nếu đăng nhập thành công
                else:
                    messages.error(request, "Incorrect password.")
                    
            except User.DoesNotExist:
                messages.error(request, "Username does not exist.")

    return render(request, 'app_home/login.html')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        # Kiểm tra trường trống
        if not request.POST.get('username') or not request.POST.get('email') or not request.POST.get('password') or not request.POST.get('confirm_password'):
            messages.error(request, "This field is required")
        elif request.POST.get('password') != request.POST.get('confirm_password'):
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username = request.POST.get('username')).exists():
            messages.error(request, "This username is already taken")
        elif not request.POST.get('email').count('@') == 1 or '.' not in request.POST.get('email'):
            messages.error(request, "Enter a valid email address")
        elif len(request.POST.get('phone')) < 10 or not request.POST.get('phone').isdigit():
            messages.error(request, "Enter a valid phone number")
        else:
            if form.is_valid():
                form.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'app_home/register.html', context)

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_home/password/password_reset.html'
    email_template_name = 'app_home/password/password_reset_email.html'
    subject_template_name = 'app_home/password/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
# Product List
def products(request):
    products = Product.objects.all()
    return render(request, 'app_home/products/products.html', {'products': products})

# Edit Product
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    categories = Category.objects.all()
    return render(request, 'app_home/products/product-edit.html', {'form': form, 'product': product, 'categories': categories})

# Delete Product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('products')  # Tên URL phải đúng như trong urls.py
    return render(request, 'app_home/products/product-delete.html', {'product': product})


# Create New Product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('products')  # Redirect to the products list
        
    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'app_home/products/products-new.html', {'form': form, 'categories': categories})
# Edit Account

def accountEdit(request, id):
    User = get_user_model()  # Dynamically get the User model
    user = get_object_or_404(User, id=id)  # Correctly fetch the user object
    
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated successfully!")
            return redirect('settings-account', id=id)  # Ensure proper redirection with user id
     
    else:
        form = UserForm(instance=user)

    return render(request, 'includes/settings-account.html', {'form': form, 'user': user})

@login_required
def deactivate_account(request):
    if request.method == "POST":
        user = request.user
        user.is_active = False  # Mark user as inactive
        user.save()
        messages.success(request, "Your account has been deactivated.")
        return redirect('home')  # Redirect to the homepage or login page
    return redirect('settings-account', id=request.user.id)
# User List
def users(request):
    users = User.objects.all()
    return render(request, 'app_home/users/users.html', {'users': users})


# Edit User



def userEdit(request, id):
  user = User.objects.get(id = id)

  template = loader.get_template('app_home/users/user-edit.html')
  context = {
    'user': user,
   
  }
  return HttpResponse(template.render(context, request))
def user_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products')
    else:
        form = UserForm(instance=user)
    return render(request, 'app_home/users/user-edit.html', {'form': form, 'user':user})
# Delete User
def userDelete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deactivated successfully!")
        return redirect('users')
    return render(request, 'app_home/users/user-delete.html', {'user': user})


# Create New User
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm()
    return render(request, 'app_home/users/user-new.html', {'form': form})

def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.order_items.all()  
        cartItems = order.get_cart_items 

        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    id = request.GET.get('id', '')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub=False)
    
    context = {
        'products': products,
        'categories': categories,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    return render(request, 'app_home/app/detail.html', context)


def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    products = Product.objects.none()  # Default to no products

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'app_home/app/category.html', context)



def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains=searched)
    else:
        searched = ""
        keys = Product.objects.none()

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    return render(request, 'app/search.html', {"searched": searched, "keys": keys, 'products': products, 'cartItems': cartItems})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer =customer, complete = False)
        items = order.order_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items= []
        order = {'get_cart_items':0,'get_cart_total':0 }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context={'categories': categories ,'items':items, 'order':order,'cartItems':cartItems,'user_not_login':user_not_login, 'user_login': user_login}
    return render(request,'app_home/app/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer =customer, complete = False)
        items = order.ordered_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items= []
        order = {'get_cart_items':0,'get_cart_total':0 }
        user_not_login = "show"
        user_login = "hidden"
        cartItems = order['get_cart_items', 'cartItems':cartItems,'user_not_login':user_not_login, 'user_login': user_login]
    context={'items':items, 'order': order}
    return render(request,'app/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId =data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer =customer, complete = False)
    orderItem, created = orderItem.objects.get_or_create(order = order, product = product) 
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added', safe=False)