import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DeleteProductTest(unittest.TestCase):
    def setUp(self):
        """Khởi tạo trình duyệt và đăng nhập"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:8000/login/")

        # Đăng nhập vào hệ thống
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("123")
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
    
    def tearDown(self):
        """Đóng trình duyệt sau khi test xong"""
        self.driver.quit()

    def test_delete_product(self):
        """Test xóa sản phẩm"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Điều hướng đến trang quản lý sản phẩm
        driver.get("http://127.0.0.1:8000/products")
        time.sleep(2)  # Đợi trang load

        # Kiểm tra danh sách sản phẩm trước khi xóa
        products_before = driver.find_elements(By.XPATH, "//table/tbody/tr")
        if len(products_before) == 0:
            self.fail("Không có sản phẩm nào để xóa!")

        # Lấy ID sản phẩm đầu tiên
        first_product_id = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]").text
        print(f" Đang xóa sản phẩm có ID: {first_product_id}")

        # Nhấn vào dropdown menu
        try:
            dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[1]/td[last()]/div/button")))
            
            # Scroll đến phần tử nếu nó nằm ngoài màn hình
            driver.execute_script("arguments[0].scrollIntoView();", dropdown_button)
            time.sleep(1)

            # Kiểm tra nếu phần tử hiển thị
            if dropdown_button.is_displayed() and dropdown_button.is_enabled():
                dropdown_button.click()
            else:
                self.fail("Dropdown button không hiển thị hoặc không thể nhấp!")
        
        except Exception as e:
            self.fail(f"Lỗi khi nhấp vào dropdown: {e}")

        time.sleep(1)

        # Click vào "Delete" trong menu
        try:
            delete_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[1]/td[last()]/div/div/a[contains(@href, 'delete-product')]")))
            delete_link.click()
        except Exception as e:
            self.fail(f"Lỗi khi nhấp vào link xóa: {e}")

        time.sleep(2)

        # Xác nhận điều hướng đến trang xóa
        try:
            delete_page_title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h4"))).text
            assert "Delete Product" in delete_page_title, "Không điều hướng đúng trang xóa!"
        except Exception as e:
            self.fail(f"Lỗi khi kiểm tra trang xóa: {e}")

        # Click nút "Delete Product"
        try:
            confirm_delete_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-danger")))
            confirm_delete_button.click()
        except Exception as e:
            self.fail(f"Lỗi khi nhấp vào nút xác nhận xóa: {e}")

        time.sleep(3)

        # Kiểm tra danh sách sản phẩm sau khi xóa
        products_after = driver.find_elements(By.XPATH, "//table/tbody/tr")
        self.assertLess(len(products_after), len(products_before), "Sản phẩm chưa bị xóa!")

        print(f" Sản phẩm có ID {first_product_id} đã bị xóa thành công!")

if __name__ == "__main__":
    unittest.main()
