from datetime import datetime
import json
from queue import Full
from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib import messages
from app_admin.models import Customer, LoyaltyCustomer, Product, Promotion, User, Category, Order, OrderItem
from .forms import OrderForm, OrderItemForm, ProductForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.template import loader
# Home Page

def home(request):
    return render(request, 'home.html')
# Thông tin bảo hành
def bao_Hanh(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer=request.user, complete=False).first()
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
    products= Product.objects.all()
    context={'products': products,'cartItems':cartItems,
             'user_not_login':user_not_login, 
             "user_login": user_login,
             'categories':categories}
    return render(request, 'app_home/app/baoHanh.html', context)
# chọn size
def choice_size(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer=request.user, complete=False).first()
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
    products= Product.objects.all()
    context={'products': products,'cartItems':cartItems,
             'user_not_login':user_not_login, 
             "user_login": user_login,
             'categories':categories}
    return render(request, 'app_home/app/choiceSize.html', context)
# huonwg daanx mua hàng
def mua_hang(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer=request.user, complete=False).first()
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
    products= Product.objects.all()
    context={'products': products,'cartItems':cartItems,
             'user_not_login':user_not_login, 
             "user_login": user_login,
             'categories':categories}
    return render(request, 'app_home/app/muaHang.html', context)
# Giới thiệu
def Gioi_Thieu(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer=request.user, complete=False).first()
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
    products= Product.objects.all()
    context={'products': products,'cartItems':cartItems,
             'user_not_login':user_not_login, 
             "user_login": user_login,
             'categories':categories}
    return render(request, 'app_home/app/GioiThieu.html', context)
def home(request):
    products = Product.objects.all()  # Lấy toàn bộ sản phẩm
    return render(request, 'home.html', {'products': products})



def app_home(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer=request.user, complete=False).first()
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
    products= Product.objects.all()
    context={'products': products,'cartItems':cartItems,
             'user_not_login':user_not_login, 
             "user_login": user_login,
             'categories':categories}
    return render(request,'app_home/app/home.html',context)

def app_home(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    categories = Category.objects.filter(is_sub=False)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items  # Số lượng sản phẩm trong giỏ hàng
        user_not_login = "hidden"
        user_login = "show"
    else:
        cartItems = 0  # Nếu chưa đăng nhập, giỏ hàng là 0
    context = {'products': products, 
               'user_not_login':user_not_login, 
                'user_login': user_login,
               'categories': categories,
               'cartItems': cartItems}
 
    return render(request, 'app_home/app/home.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('home')
        return redirect('app_home/app/home.html')  # Chuyển hướng nếu đã đăng nhập

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
# order List
def orders(request):
    orders = Order.objects.all()
    return render(request, 'app_home/orders/orders.html', {'orders': orders})
def order_user(request):
    orders = Order.objects.all()
    return render(request, 'app_home/orders/order-user.html', {'orders': orders})
#order-new
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)  # Dùng OrderForm thay vì Order
        if form.is_valid():
            form.save()
            messages.success(request, "Order added successfully!")  # Đổi thông báo
            return redirect('orders')  # Chuyển hướng đến danh sách đơn hàng
        
    else:
        form = OrderForm()  # Dùng OrderForm thay vì ProductForm
    categories = Category.objects.all()
    
    return render(request, 'app_home/orders/order-new.html', {'form': form, 'categories': categories})
# Edit order
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        order.address = request.POST.get("address", order.address)
        order.complete = request.POST.get("status") == "completed"
        order.save()
        return redirect("orders")  # Chuyển hướng sau khi lưu thành công
    return render(request, "app_home/orders/order-edit.html", {"order": order})



def update_order_item(request, id):
    item = get_object_or_404(OrderItem, id=id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 0))
        if quantity > 0:
            item.quantity = quantity
            item.save()
            messages.success(request, "Order item updated successfully!")
        else:
            item.delete()  # Nếu số lượng = 0 thì xóa luôn sản phẩm khỏi giỏ hàng
    return redirect('edit-order', id=item.order.id)  # Chuyển hướng lại trang chỉnh sửa đơn hàng

# lịch sử mua hàng
def lich_Su(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
        categories = Category.objects.filter(is_sub=False)
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    context = {
        'categories': categories,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    orders = Order.objects.all()
    return render(request, 'app_home/app/lichSu.html', {'orders': orders})
# order List
def orders(request):
    orders = Order.objects.all()
    return render(request, 'app_home/orders/orders.html', {'orders': orders})
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        order.delete()
        messages.success(request, "Order deleted successfully!")
        return redirect('orders')  # Tên URL phải đúng như trong urls.py
    return render(request, 'app_home/orders/order-delete.html', {'order': order})
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
    user = User.objects.get(id = id)
    
    template = loader.get_template('app_home/settings-account.html')
    context = {
    'user': user,
   
  }
    return HttpResponse(template.render(context, request))

    

@login_required
def deactivate_account(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.gender = request.POST.get("gender")
        user.birth_date = request.POST.get("birth_date")

        if "image" in request.FILES:
            user.image = request.FILES["image"]

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("settings-account", id=user.id)

    return render(request, "app_home/settings-account.html", {"user": user})

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
    user = get_object_or_404(User, id=id)  # Lấy user cần chỉnh sửa

    if request.method == "POST":
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        user.gender = request.POST.get('gender', user.gender)
        user.birth_date = request.POST.get('birth_date', user.birth_date)
        user.role = request.POST.get('role', user.role)

        password = request.POST.get('password', '')
        if password:  # Nếu nhập mật khẩu mới, cần mã hóa trước khi lưu
            user.password = password

        if 'image' in request.FILES:  # Nếu có hình ảnh mới, lưu lại
            user.image = request.FILES['image']

        user.save()  # Lưu thay đổi vào database
        messages.success(request, "User updated successfully!")
        return redirect('users')  # Điều hướng về trang danh sách user

    return render(request, 'app_home/users/user-edit.html', {'user': user})
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
            user = form.save(commit=False)  # Chưa lưu ngay vào DB
            user.set_password(form.cleaned_data['password'])  # Mã hóa mật khẩu
            user.save()
            messages.success(request, "User created successfully!")
            return redirect('users')
        else:
            messages.error(request, "Please correct the errors below.")
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


# Cart Page
@login_required
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.order_items.all()
    cartItems = order.get_cart_items
    categories = Category.objects.filter(is_sub=False)

    context = {
        'categories': categories,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'app_home/app/cart.html', context)
#loyalty
def loyalty_customers(request):
    customers = LoyaltyCustomer.objects.select_related("customer").all()

    return render(request, "app_home/loyaltys/loyalty.html", {"customers": customers})
# add khách hàng thân thiết
def new_loyalty_customer(request):
    customers = Customer.objects.select_related("user").all()  # Lấy danh sách khách hàng kèm user
    promotions = Promotion.objects.all()  # Lấy danh sách khuyến mãi

    return render(request, "app_home/loyaltys/new-loyaltys.html", {
        "customers": customers,
        "promotions": promotions
    })

# xóa khách hàng thân thiết đã dùng mã giảm giá


def delete_customer(request, id):
    loyalty_customer = get_object_or_404(LoyaltyCustomer, id=id)  # Lấy khách hàng từ LoyaltyCustomer

    if request.method == "POST":
        loyalty_customer.delete()
        return redirect("customers")  

    return render(request, "app_home/loyaltys/loyalty.html", {"loyalty_customer": loyalty_customer})
# chỉnh  sửa khách hàng thân thiết
def edit_loyalty_customer(request, id):
    customer = get_object_or_404(LoyaltyCustomer, id=id)
    promotions = Promotion.objects.all()  # Lấy danh sách khuyến mãi

    if request.method == "POST":
        eligible_date = request.POST.get("eligible_date")
        points_required = request.POST.get("points_required")
        points = request.POST.get("point")
        promotion_id = request.POST.get("promotion")

        # Validate and parse the inputs correctly
        if eligible_date:
            eligible_date = datetime.strptime(eligible_date, "%Y-%m-%d").date()
        if points_required:
            points_required = int(points_required)
        if points:
            points = int(points)
        
        # Update the customer data
        customer.eligible_date = eligible_date
        customer.points_required = points_required
        customer.point = points  

        # Handle promotion
        if promotion_id:
            customer.promotion = get_object_or_404(Promotion, id=promotion_id)

        customer.save()
        return redirect('loyalty')

    return render(request, "app_home/loyaltys/edit_loyalty.html", {
        "customer": customer,
        "promotions": promotions
    })
# Product Search
def search(request):
    searched = request.GET.get("search", "").strip()  # Lấy từ khóa từ GET thay vì POST
    keys = Product.objects.filter(name__icontains=searched) if searched else Product.objects.none()

    categories = Category.objects.filter(is_sub=False)
    cartItems = 0

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items

    return render(request, 'app_home/app/search.html', {
        'categories': categories,
        'searched': searched,
        'keys': keys,
        'cartItems': cartItems
    })




# Checkout Page
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
        categories = Category.objects.filter(is_sub=False)
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"

    context = {
        'categories': categories,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    return render(request, 'app_home/app/checkout.html', context)


# Update Cart Item (AJAX)
def updateItem(request):
    try:
        data = json.loads(request.body)
        productId = data.get('productId')
        action = data.get('action')

        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User not logged in'}, status=401)

        customer = request.user
        product = Product.objects.get(id=productId)

        # Tạo đơn hàng nếu chưa có
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'quantity': 0})

        # Cập nhật số lượng sản phẩm
        if action == 'add':
            orderItem.quantity += 1
        elif action == 'remove':
            orderItem.quantity -= 1

        # Lưu cập nhật hoặc xóa nếu số lượng = 0
        if orderItem.quantity > 0:
            orderItem.save()
        else:
            orderItem.delete()

        return JsonResponse({'message': 'Updated successfully', 'quantity': orderItem.quantity if orderItem.quantity > 0 else 0}, safe=False)
    
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)