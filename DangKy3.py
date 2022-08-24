from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="venv/chromedriver")
driver.get('https://tiki.vn/')

driver.set_window_size(1400, 800)
try:
    driver.find_element(By.CSS_SELECTOR, '.account-label > span').click()
    driver.implicitly_wait(15)

    driver.find_element(By.NAME, 'tel').click()
    driver.find_element(By.NAME, 'tel').send_keys("0567536156")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

#Nhập mã xác minh sai
    sl = driver.find_elements(By.CSS_SELECTOR, '.otp-container input')
    for s in sl[:6]:
        s.send_keys(9)
    driver.find_element(By.XPATH, "//*[text()='Xác Minh']").click()
    ins = driver.find_element(By.XPATH, "//*[text()='Mã xác thực không đúng hoặc đã hết hạn']").text
    print(ins)

except NoSuchElementException:
    print("Loi")

driver.quit()