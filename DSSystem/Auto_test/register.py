import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class DjangoRegisterTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Đóng trình duyệt sau mỗi bài kiểm thử
        self.driver.quit()

    def test_register_success(self):
        """TH1: Nhập thông tin hợp lệ, đăng ký thành công"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        # Điền thông tin đăng ký hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(3)
        # Kiểm tra chuyển hướng thành công sau khi đăng ký
        self.assertIn("Registration successful", driver.find_element(By.TAG_NAME, "body").text)

    def test_register_password_mismatch(self):
        """TH2: Nhập mật khẩu và xác nhận mật khẩu không khớp"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        # Điền thông tin nhưng mật khẩu không khớp
        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("wrongpassword")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(3)
        # Kiểm tra thông báo lỗi mật khẩu không khớp
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Passwords do not match", error_message)

    def test_register_empty_fields(self):
        """TH3: Không điền thông tin nào, đăng ký thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        # Nhấn nút đăng ký mà không điền thông tin
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(3)
        # Kiểm tra thông báo lỗi khi không điền thông tin
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("All fields are required", error_message)

    def test_register_invalid_email(self):
        """TH4: Nhập email không hợp lệ"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        # Điền email không hợp lệ
        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("invalidemail")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(3)
        # Kiểm tra thông báo lỗi email không hợp lệ
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Enter a valid email address", error_message)

if __name__ == "__main__":
    unittest.main()
