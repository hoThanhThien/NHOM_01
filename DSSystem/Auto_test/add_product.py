import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class ProductFormTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Đợi tối đa 5 giây để phần tử xuất hiện
        self.driver.get("http://127.0.0.1:8000/login/")

        # Đăng nhập
        self.driver.find_element(By.NAME, "username").send_keys("ad")
        self.driver.find_element(By.NAME, "password").send_keys("123")
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()

        # Điều hướng đến trang thêm sản phẩm
        self.driver.get("http://127.0.0.1:8000/products-new")

    def tearDown(self):
        # Đóng trình duyệt sau mỗi bài kiểm thử
        self.driver.quit()

    def test_submit_product_form(self):
        """Test form submission with valid inputs"""
        driver = self.driver
        
        # Điền thông tin sản phẩm
        driver.find_element(By.NAME, "name").send_keys("Diamond Ring")
        
        # Chọn danh mục
        category_select = Select(driver.find_element(By.NAME, "category"))
        category_select.select_by_index(1)  # Chọn danh mục đầu tiên (tránh chọn option rỗng)
        
        driver.find_element(By.NAME, "carat_weight").send_keys("1.25")
        driver.find_element(By.NAME, "size_ni").send_keys("11")
        driver.find_element(By.NAME, "diamond_origin").send_keys("South Africa")
        driver.find_element(By.NAME, "price").send_keys("1500")
        driver.find_element(By.NAME, "provider").send_keys("Best Diamonds Co.")
        driver.find_element(By.NAME, "quantity").send_keys("10")
        time.sleep(3)

        driver.find_element(By.NAME, "descriptions").send_keys("High-quality diamond ring for special occasions.")
        time.sleep(3)

        # Upload ảnh sản phẩm
        image_path = "C:\\Users\\DELL\\OneDrive - ut.edu.vn\\BanPTTKHT_DiamondShopSystem\\SRC\\P1\\NHOM_01\\DSSystem\\app_home\\static\\app_home\\assets\\img\\img_can_add\\7I10-3.webp"
        driver.find_element(By.NAME, "image").send_keys(image_path)

        # Đánh dấu sản phẩm là "Active"
        active_checkbox = driver.find_element(By.NAME, "active")
        if not active_checkbox.is_selected():
            active_checkbox.click()

        # Gửi biểu mẫu
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

  
       
        page_text = driver.find_element(By.TAG_NAME, "body").text
        print(page_text)  # In nội dung để kiểm tra
        self.assertIn("Products / Manage Products", page_text)
if __name__ == "__main__":
    unittest.main()
