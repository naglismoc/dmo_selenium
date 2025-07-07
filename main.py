'''
Pirma paleidžiam šitą komandos eilutę terminale
pip install selenium
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,5)
driver.get("https://www.skelbiu.lt/skelbimai/?keywords=karpis")
wait.until(expected_conditions.visibility_of_element_located((By.ID,'onetrust-accept-btn-handler'))).click()

# sausainuku_mygtukas = driver.find_element(By.ID, 'onetrust-accept-btn-handler') #grazino web elementa
# sausainuku_mygtukas.click()




# a_list = driver.find_element(By.CLASS_NAME,'standard-list-container').find_elements(By.TAG_NAME,'a')
# urls = []
# for a in a_list:
#     urls.append(a.get_attribute("href"))
#     print(a.get_attribute("href"))
#
# # print(urls)
# for url in urls:
#     driver.get(url)
#============================== paieska ======================
# driver.find_element(By.ID, 'searchKeyword').send_keys("lova")
# driver.find_element(By.NAME, 'submit_bn').click()
# # time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="popular_categories_by_keyword"]/div[1]/a[4]').click()
#============================== paieska ======================


#============================== kategorijų nuorodų nurinkimas į sarašą ======================
# main_container = driver.find_element(By.ID, 'main-categories-container')
# cage_blocks = main_container.find_elements(By.CLASS_NAME,'categBlock')
# hrefs = []
# for cb in cage_blocks:
#     for a in cb.find_elements(By.TAG_NAME, 'a'):
#         hrefs.append(a.get_attribute("href"))
# print(hrefs)
#============================== kategorijų nuorodų nurinkimas į sarašą ======================

input()

# time.sleep(600)
# driver.quit()