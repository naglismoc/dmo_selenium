import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://skelbiu.lt")
sausainuku_mygtukas = driver.find_element(By.ID, 'onetrust-accept-btn-handler') #grazino web elementa
sausainuku_mygtukas.click()

driver.find_element(By.ID, 'searchKeyword').send_keys("lova")
driver.find_element(By.NAME, 'submit_bn').click()
# time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="popular_categories_by_keyword"]/div[1]/a[4]').click()


time.sleep(120)
driver.quit()