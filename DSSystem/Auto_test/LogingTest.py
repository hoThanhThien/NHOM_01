import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class DjangoTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Đóng trình duyệt sau mỗi bài kiểm thử
        self.driver.quit()

    def test_login_correct_credentials(self):
        """TH3: Nhập đúng username và password, login thành công"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login/")

        # Điền thông tin đăng nhập đúng
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(5)
        # Kiểm tra tiêu đề trang sau khi đăng nhập thành công
        self.assertEqual(driver.title, "Dashboard DSSystem")

    def test_login_wrong_password(self):
        """TH1: Nhập đúng username nhưng sai password, login thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login/")

        # Nhập username đúng và password sai
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(5)
        # Kiểm tra thông báo lỗi
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Invalid username or password", error_message)

    def test_login_wrong_username(self):
        """TH2: Nhập username sai và password đúng, login thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login/")

        # Nhập username sai và password đúng
        driver.find_element(By.NAME, "username").send_keys("wronguser")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(5)
        # Kiểm tra thông báo lỗi
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Invalid username or password", error_message)

    def test_login_empty_credentials(self):
        """TH4: Không nhập gì cả, login thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login/")

        # Nhấn nút login mà không nhập thông tin
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(5)
        # Kiểm tra thông báo lỗi
        error_message = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Please fill in both username and password fields.", error_message)

if __name__ == "__main__":
    unittest.main()