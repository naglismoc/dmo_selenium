import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

driver.get("https://www.delfi.lt")

driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "live-stream-announcement__close"))).click()
# driver.find_element(By.ID, "i5").click()

time.sleep(500)
