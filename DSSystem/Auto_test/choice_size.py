import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class ChoiceSizeTest(unittest.TestCase):
    def setUp(self):
        """Khởi tạo WebDriver"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Đợi tối đa 10 giây để phần tử xuất hiện
        self.driver.get("http://127.0.0.1:8000/choiceSize/")  # Điều hướng đến trang chọn size nhẫn

    def tearDown(self):
        """Đóng trình duyệt sau mỗi bài kiểm thử"""
        self.driver.quit()

    def test_calculate_ring_size(self):
        """Test nhập chu vi ngón tay và tính toán size nhẫn"""
        driver = self.driver

        # Nhập chu vi ngón tay
        finger_size_input = driver.find_element(By.ID, "fingerSize")
        finger_size_input.clear()
        finger_size_input.send_keys("55")  # Nhập số đo hợp lệ

        # Nhấn nút tính toán
        driver.find_element(By.CLASS_NAME, "calculate-btn").click()
        time.sleep(2)  # Chờ kết quả hiển thị

        # Kiểm tra xem kết quả đã xuất hiện chưa
        result_div = driver.find_element(By.ID, "result")
        result_text = result_div.text
        print(result_text)  # In kết quả để kiểm tra

        # Kiểm tra nội dung kết quả có đúng không
        self.assertIn("Chu vi ngón tay: 55.0 mm", result_text)
        self.assertIn("Size nhẫn phù hợp: 16", result_text)

if __name__ == "__main__":
    unittest.main()
