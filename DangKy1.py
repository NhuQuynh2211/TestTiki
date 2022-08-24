from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/')
#Nhập sai định dạng số điện thoại
driver.set_window_size(1400, 800)
try:
    driver.find_element(By.CSS_SELECTOR, '.account-label > span').click()
    driver.implicitly_wait(15)

    driver.find_element(By.NAME, 'tel').click()
    driver.find_element(By.NAME, 'tel').send_keys("05657616156")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

    inra = driver.find_element(By.XPATH, "//*[text()='Số điện thoại không đúng định dạng. ']").text
    print(inra)

except NoSuchElementException:
    print("Loi")

driver.quit()