from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/do-an-vat/c4421')

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
    driver.execute_script("window.scrollBy(0,300)", "")

    sl = driver.find_element(By.CLASS_NAME, 'input')

    sl.clear()
    sl.send_keys(3)
    dis = driver.find_element(By.CSS_SELECTOR, '[alt="remove-icon"]')
    dis.click()

print(links)
#driver.quit()
#Nhấn - Giảm số lượng
