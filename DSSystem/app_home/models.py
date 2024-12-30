from django.db import models

# Create your models here.

# Role model
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Employee model
class Employee(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return f"Employee {self.id} - Role: {self.role.name}"

# User model
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.BooleanField()  # True for male, False for female
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")

    def __str__(self):
        return f"Customer: {self.user.username}"

# LoyaltyCustomer model
class LoyaltyCustomer(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="loyalty_details")
    eligible_date = models.DateField()
    points_required = models.IntegerField()
    promotion = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Loyalty Program - {self.customer.user.username}"

# Promotion model
class Promotion(models.Model):
    discount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Promotion {self.id} - {self.discount}%"

# Category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    carat_weight = models.FloatField()
    diamond_origin = models.CharField(max_length=100)
    price = models.FloatField()
    provider_id = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    order_date = models.DateField(auto_now_add=True)
    ship_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)  # False for incomplete, True for complete

    def __str__(self):
        return f"Order {self.id} - Customer: {self.customer.user.username if self.customer else 'N/A'}"

# OrderDetail model
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_details")
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order.id} - Product: {self.product.name}"