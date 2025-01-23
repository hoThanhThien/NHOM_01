import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ProductFormTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login/")

        # Đăng nhập trước khi thực hiện kiểm thử
        self.driver.find_element(By.NAME, "username").send_keys("ad")
        self.driver.find_element(By.NAME, "password").send_keys("a")
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)

        # Điều hướng đến trang thêm sản phẩm
        self.driver.get("http://http://127.0.0.1:8000/products-new")
        self.driver.find_element(By.CLASS_NAME, "menu-item active").click()
        time.sleep(2)

    def tearDown(self):
        # Đóng trình duyệt sau mỗi bài kiểm thử
        self.driver.quit()

    def test_submit_product_form(self):
        """Test form submission with valid inputs"""

        driver = self.driver

        # Điền thông tin sản phẩm
        driver.find_element(By.NAME, "product_id").send_keys("P12345")
        driver.find_element(By.NAME, "name").send_keys("Diamond Ring")
        driver.find_element(By.NAME, "category").send_keys(Keys.ARROW_DOWN, Keys.ENTER)  # Chọn danh mục đầu tiên
        driver.find_element(By.NAME, "carat_weight").send_keys("1.25")
        driver.find_element(By.NAME, "size_ni").send_keys("5.5")
        driver.find_element(By.NAME, "diamond_origin").send_keys("South Africa")
        driver.find_element(By.NAME, "price").send_keys("1500")
        driver.find_element(By.NAME, "provider").send_keys("Best Diamonds Co.")
        driver.find_element(By.NAME, "quantity").send_keys("10")
        driver.find_element(By.NAME, "descriptions").send_keys("High-quality diamond ring for special occasions.")

        # Upload ảnh sản phẩm
        image_path = "app_home/static/app_home/assets/img/img_can_add/7I10-3.webp"  # Đường dẫn đến ảnh mẫu
        driver.find_element(By.NAME, "image").send_keys(image_path)

        # Đánh dấu sản phẩm là "Active"
        active_checkbox = driver.find_element(By.NAME, "active")
        if not active_checkbox.is_selected():
            active_checkbox.click()

        # Gửi biểu mẫu
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(5)

        # Kiểm tra nếu form được gửi thành công
        body_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Product successfully added", body_text)
if __name__ == "__main__":
    unittest.main()