import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)  # Thời gian chờ mặc định

    def tearDown(self):
        self.driver.quit()

    def test_register_valid(self):
        """TH1: Nhập đúng, thành công"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "first_name").send_keys("New")
        driver.find_element(By.NAME, "last_name").send_keys("User")
        driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "phone").send_keys("0123456789")
        Select(driver.find_element(By.NAME, "gender")).select_by_visible_text("Male")
        driver.find_element(By.NAME, "birth_date").send_keys("01/01/2000")

        time.sleep(5)
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)

        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
            ).text
            self.assertIn("Registration successful", success_message)
            self.assertIn("login", driver.current_url)
        except TimeoutException:
            self.fail("Registration success message not displayed in time.")

   

    def test_register_invalid_email(self):
        """TH2: Nhập email sai, thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("invalidemail")
        driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("SecurePassword123")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        ).text
        self.assertIn("Enter a valid email address", error_message)

    def test_register_password_mismatch(self):
        """TH3: Nhập password không khớp, thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("DifferentPassword123")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        ).text
        self.assertIn("Passwords do not match", error_message)

    def test_register_empty_fields(self):
        """TH4: Nhập bỏ trống, thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        driver.find_element(By.NAME, "username").send_keys("")
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.NAME, "confirm_password").send_keys("")
        driver.find_element(By.NAME, "phone").send_keys("")  # Số điện thoại không hợp lệ

        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        ).text
        self.assertIn("This field is required", error_message)

    def test_register_invalid_phone(self):
        """TH5: Nhập sdt không hợp lệ, thất bại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuserPhone")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "phone").send_keys("abcd1234")  # Số điện thoại không hợp lệ
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)

        error_message = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        ).text
        self.assertIn("Enter a valid phone number", error_message)
    def test_register_username(self):
        """TH3: Nhập đúng username và password nhưng username đã tồn tại"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "email").send_keys("thienht2941@ut.edu.vn")
        driver.find_element(By.NAME, "first_name").send_keys("Hồ")
        driver.find_element(By.NAME, "last_name").send_keys("Thiện")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "confirm_password").send_keys("123")
        driver.find_element(By.NAME, "phone").send_keys("0375227764")
        Select(driver.find_element(By.NAME, "gender")).select_by_visible_text("Male")
        driver.find_element(By.NAME, "birth_date").send_keys("01/01/2005")

        time.sleep(5)
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))
        time.sleep(5)
        error_message = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        ).text
        self.assertIn("This username is already taken", error_message)
        
if __name__ == "__main__":
    unittest.main()
