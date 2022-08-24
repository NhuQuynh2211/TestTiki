from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/do-an-vat/c4421')

driver.set_window_size(1400, 800)
products = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.product-item'))
)
links = []
for p in products[:1]:
    try:
        links.append(p.get_attribute('href'))
        print(p.find_element(By.CLASS_NAME, 'name').text)
    except StaleElementReferenceException:
        pass

for l in links:
    driver.get(l)
    Nhap = driver.find_element(By.CLASS_NAME, 'input')
    str = input("Nhap so luong: ")

    driver.execute_script("window.scrollBy(0,300)", "")
    driver.implicitly_wait(40)

    Nhap.clear()
    Nhap.send_keys(str)

print(links)
# driver.quit()
# nhập số lượng
# đầu vào là mình sẽ nhập số lượng vào