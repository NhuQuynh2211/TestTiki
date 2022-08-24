from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/bach-hoa-online/c4384')

products = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.product-item'))
)
#Đổi địa chỉ xem chi phí vận chuyển không đăng nhập
links = []
for p in products[:1]:
    try:
        links.append(p.get_attribute('href'))
        print(p.find_element(By.CLASS_NAME, 'name').text)
    except StaleElementReferenceException:
        pass
for l in links:
    driver.get(l)

    driver.set_window_size(1400,900)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[text()= 'Đổi địa chỉ']").click()

    driver.find_element(By.XPATH, "//*[text()= 'Chọn khu vực giao hàng khác']").click()

    driver.find_element(By.XPATH, "//*[text()= 'Vui lòng chọn tỉnh/thành phố']").click()
    driver.find_element(By.ID, "react-select-2-option-0").click()

    driver.find_element(By.XPATH, "//*[text()= 'Vui lòng chọn quận/huyện']").click()
    driver.find_element(By.ID, "react-select-3-option-14").click()

    driver.find_element(By.XPATH, "//*[text()= 'Vui lòng chọn phường/xã']").click()
    driver.find_element(By.ID, "react-select-4-option-1").click()

    driver.find_element(By.XPATH, "//*[text()= 'GIAO ĐẾN ĐỊA CHỈ NÀY']").click()

print(links)
#driver.quit()
