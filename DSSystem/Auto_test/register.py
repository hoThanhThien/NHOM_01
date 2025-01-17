import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_register_valid(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "first_name").send_keys("New")
        driver.find_element(By.NAME, "last_name").send_keys("User")
        driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("SecurePassword123")
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        Select(driver.find_element(By.NAME, "gender")).select_by_visible_text("Male")
        driver.find_element(By.NAME, "birth_date").send_keys("2000-01-01")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

       

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        ).text
        self.assertIn("Registration successful! You can now log in", success_message)

    def test_register_invalid_email(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("invalidemail@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

        time.sleep(7)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Enter a valid email address", error_message)

    def test_register_password_mismatch(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("DifferentPassword123")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

        time.sleep(7)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Passwords do not match", error_message)

    def test_register_empty_fields(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

        time.sleep(7)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("This field is required", error_message)

    def test_register_duplicate_username(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("ExistingUser123")
        driver.find_element(By.NAME, "email").send_keys("existinguser@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

        time.sleep(7)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Passwords do not match", error_message)

    def test_register_invalid_phone(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")

        driver.find_element(By.NAME, "username").send_keys("newuser")
        driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("securepassword")
        driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "btn-primary"))

        time.sleep(7)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Passwords do not match", error_message)

if __name__ == "__main__":
    unittest.main()