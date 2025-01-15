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


