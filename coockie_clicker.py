import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://ozh.github.io/cookieclicker/')

#clicking language option
english_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#langSelect-EN'))
)
english_option.click()

#Detecting Cookie
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bigCookie')))
cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')

def click_cookie():
    cookie.click()

def buy_products():
    products = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
    for product in products[::-1]:
        product.click()
        time.sleep(0.05)

def buy_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, 'upgrade.enabled')
    for upgrade in upgrades:
        upgrade.click()
        time.sleep(0.05)


start_time = time.time()
timeout = 60*10

while True:
    click_cookie()

    if time.time() % 5 < 0.01:
        buy_products()
        buy_upgrades()
    time.sleep(0.01)
    if time.time() - start_time > timeout:
        break

driver.quit()





