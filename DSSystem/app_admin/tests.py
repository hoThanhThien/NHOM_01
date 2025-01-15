from django.test import TestCase
from django.utils.timezone import now
from .models import User, Customer, LoyaltyCustomer, Promotion, Category, Product, Order, OrderDetail

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username="testuser",
            password="test123",
            role="customer",
            phone="123456789",
            gender="male"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.role, "customer")
        self.assertTrue(user.check_password("test123"))

class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        user = User.objects.create_user(username="testcustomer", password="test123")
        customer = Customer.objects.create(user=user)
        self.assertEqual(customer.user.username, "testcustomer")

