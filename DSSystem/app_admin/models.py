from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.admin.models import LogEntry



# Gender Choices
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

# Custom User Model
class User(AbstractUser):
    ROLES = (
        ('customer', 'Customer'),
        ('sales', 'Sales Staff'),
        ('delivery', 'Delivery Staff'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='customer')
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='app_home/static/app_home/assets/img/avatars/')
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=200)
    # Many-to-Many Relationship with Product (if required)
    products = models.ManyToManyField('Product', blank=True, related_name="users")

    # Avoid conflicts by defining custom related_name
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
    )

    def __str__(self):
        return f"{self.id} - {self.username}"


# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")

    def __str__(self):
        return f"Customer: {self.user.username}"


# LoyaltyCustomer Model
class LoyaltyCustomer(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="loyalty_details")
    eligible_date = models.DateField()
    points_required = models.IntegerField()
    promotion = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Loyalty Program - {self.customer.user.username}"


# Promotion Model
class Promotion(models.Model):
    discount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Promotion {self.id} - {self.discount}%"


# Category Model
class Category(models.Model):
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
   


# Product Model
class Product(models.Model):
    #product_id = models.CharField(max_length=100, unique=True, default='default_product_id')
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    carat_weight = models.FloatField(null=True, blank=True)
    size_ni = models.FloatField(null=True, blank=True)
    diamond_origin = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()
    provider = models.CharField(max_length=200, default='default_provider')
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='app_home/static/app_home/assets/img/product_images/')
    update_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.id} - {self.name}"

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    ship_date = models.DateTimeField(null=True, blank=True)  # Thêm ngày giao hàng
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"Order {self.id} - {self.customer}"

    @property
    def get_cart_items(self):  
        return sum(item.quantity for item in self.order_items.all())
 

    @property
    def get_cart_total(self):
        return sum(item.get_total for item in self.order_items.all())

class OrderItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total
