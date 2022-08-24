from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/')
#khong nhap ma xac minh
driver.set_window_size(1400, 800)
try:
    driver.find_element(By.CSS_SELECTOR, '.account-label > span').click()
    driver.implicitly_wait(15)

    driver.find_element(By.NAME, 'tel').click()
    driver.find_element(By.NAME, 'tel').send_keys("0567616156")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

    driver.find_element(By.XPATH, "//*[text()='Xác Minh']").click()
    noMa = driver.find_element(By.XPATH, "//*[text()='Vui lòng nhập mã xác minh(OTP)']").text
    print(noMa)

except NoSuchElementException:
    print("Loi")

driver.quit()