import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from app_admin.models import Product, User, Category, Order
from .forms import ProductForm, UserForm


# Home Pageâ
def home(request):
    return render(request, 'home.html')
def app_home(request):
    return render(request, 'app_home/app/home.html')
def logoutPage(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Nếu đã đăng nhập, chuyển hướng về trang chủ

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username and not password:
            messages.error(request, "Please fill in both username and password fields.")
        elif not username:
            messages.error(request, "Please enter your username.")
        elif not password:
            messages.error(request, "Please enter your password.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid username or password.")
            else:
                login(request, user)
                return redirect('home')

    return render(request, 'app_home/login.html')
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
            return redirect('product-list')
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
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'app_home/products/products-new.html', {'form': form, 'categories': categories})
# User List
def users(request):
    users = User.objects.all()
    return render(request, 'app_home/users/users.html', {'users': users})

# Edit User
def userEdit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('users')
    else:
        form = UserForm(instance=user)
    return render(request, 'app_home/users/user-edit.html', {'form': form, 'user': user})

# Delete User
def userDelete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.active = False
        user.save()
        messages.success(request, "User deactivated successfully!")
        return redirect('users')
    return render(request, 'app_home/users/user-delete.html', {'user': user})

# Create New Users

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to the "users" page
    else:
        form = UserForm()
    return render(request, 'app_home/users/user-new.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'app_home/users/users.html', {'users': users})
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
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
    return render(request, 'app/detail.html', context)

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
    return render(request, 'app/category.html', context)

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

def register(request):
    form = UserForm()
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'app_home/register.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer =customer, complete = False)
        items = order.orderitem_set.all()
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
    return render(request,'app/cart.html',context)
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