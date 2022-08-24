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
#Nhấn + tăng sl
links = []
for p in products[:1]:
    try:
        links.append(p.get_attribute('href'))
        print(p.find_element(By.CLASS_NAME, 'name').text)
    except StaleElementReferenceException:
        pass
for l in links:
    driver.get(l)

    stt = driver.find_element(By.CSS_SELECTOR, '[alt="add-icon"]')
    stt.click()
    stt.click()

    driver.find_element(By.CLASS_NAME, 'group-button').click()

    driver.implicitly_wait(5)
print(links)
driver.quit()

