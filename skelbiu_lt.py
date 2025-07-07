'''karpis
dezodorantas
bleebloo
samsung'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
search_keyword = 'bleebloo'
def set_up():
    driver.maximize_window()
    driver.implicitly_wait(5)
    accept_cookies()

def tear_down():
    # driver.close()
    input()

def accept_cookies():
    driver.get("https://www.skelbiu.lt/")
    driver.find_element(By.ID,'onetrust-reject-all-handler').click()

def get_urls():
    urls = []
    for page in range(1, 200):
        url = f'https://www.skelbiu.lt/skelbimai/{page}?keywords={search_keyword}'
        driver.get(url)
        if driver.current_url != url.replace(" ", "%20"):
            break
        cards = driver.find_element(By.CLASS_NAME, 'standard-list-container').find_elements(By.TAG_NAME, 'a')

        for card in cards:
            urls.append(card.get_attribute("href"))
    return urls

def gather_data(urls):
    for url in urls:
        print(driver.current_url)
        driver.get(url)
    # cia galima nurinkineti duomenis
def skelbiu_lt():
    set_up() #paruosiamieji darbai
    urls = get_urls()
    gather_data(urls)
    tear_down() #uzbaigimas kodo.

skelbiu_lt()
























