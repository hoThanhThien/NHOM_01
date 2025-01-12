from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

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
    role = models.CharField(max_length=10, choices=ROLES, default='customer')
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='user_images/')
    #id = models.CharField(max_length=12, unique=True)
    active = models.BooleanField(default=True)

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
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,related_name='sub_categories',null=True,blank=True)
    is_sub = models.BooleanField(default=False)
    name =  models.CharField(max_length=200,null= True)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    carat_weight = models.FloatField(null=True, blank=True)
    diamond_origin = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    provider_id = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='product_images/')
    update_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    order_date = models.DateField(auto_now_add=True)
    ship_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)  # False for incomplete, True for complete
    products = models.ManyToManyField(Product)
    def __str__(self):
        return f"Order {self.id} - Customer: {self.customer.user.username if self.customer else 'N/A'}"


# OrderDetail Model
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_details")
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order.id} - Product: {self.product.name}"
