'''
Pirma paleidžiam šitą komandos eilutę terminale
pip install selenium
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://skelbiu.lt")
sausainuku_mygtukas = driver.find_element(By.ID, 'onetrust-accept-btn-handler') #grazino web elementa
sausainuku_mygtukas.click()

#============================== paieska ======================
# driver.find_element(By.ID, 'searchKeyword').send_keys("lova")
# driver.find_element(By.NAME, 'submit_bn').click()
# # time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="popular_categories_by_keyword"]/div[1]/a[4]').click()
#============================== paieska ======================


#============================== kategorijų nuorodų nurinkimas į sarašą ======================
main_container = driver.find_element(By.ID, 'main-categories-container')
cage_blocks = main_container.find_elements(By.CLASS_NAME,'categBlock')
hrefs = []
for cb in cage_blocks:
    for a in cb.find_elements(By.TAG_NAME, 'a'):
        hrefs.append(a.get_attribute("href"))
print(hrefs)
#============================== kategorijų nuorodų nurinkimas į sarašą ======================

time.sleep(600)
driver.quit()