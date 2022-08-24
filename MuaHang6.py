from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/thuc-pham-dong-hop-va-kho/c15074')

products = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.product-item'))
)
#Chọn mua khi chưa đăng nhập trước
links = []
for p in products[:1]:
    try:
        links.append(p.get_attribute('href'))
        print(p.find_element(By.CLASS_NAME, 'name').text)
    except StaleElementReferenceException:
        pass
for l in links:
    print(links)
    driver.get(l)
    driver.implicitly_wait(15)
    driver.set_window_size(1400, 800)
    driver.find_element(By.CLASS_NAME, 'group-button').click()

    driver.find_element(By.NAME, 'tel').click()
    driver.find_element(By.NAME, 'tel').send_keys("0966892340")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

    driver.find_element(By.CSS_SELECTOR, 'body input[type=password]').click()
    driver.find_element(By.CSS_SELECTOR, 'body input[type=password]').send_keys("Tnq11221122")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

    status = driver.find_element(By.XPATH, "//*[text()= 'Thêm vào giỏ hàng thành công!']").text
    print(status)

#driver.quit()
