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
    driver.find_element(By.NAME, 'tel').send_keys("0356078311")
    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

#Đăng kí tài khoản
    sl = driver.find_elements(By.CSS_SELECTOR, '.otp-container input')
    for s in sl[:6]:
        str = input("Nhap so: ")
        s.send_keys(str)
    driver.find_element(By.XPATH, "//*[text()='Xác Minh']").click()

    driver.find_element(By.NAME, 'name').send_keys(" Như Quỳnh")
    driver.find_element(By.CSS_SELECTOR, 'body input[type=password]').send_keys("Tnq11221122")

    driver.find_element(By.CSS_SELECTOR, 'form > button').click()

except NoSuchElementException:
    print("Loi")

print(" Tao tai khoan thanh cong")
driver.close()
