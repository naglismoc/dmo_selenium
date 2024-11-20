import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class ElentaTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.acceptCookies()

    def test_positive(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(f"Jurgio pyragai{random.randint(1000,9999)}" )
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000,9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/h1/b').text
        expected_text = 'Jūs sėkmingai prisiregistravote!'

        self.assertEqual(actual_text, expected_text)

    def test_mismatching_correct_password(self):
        self.driver.get("https://elenta.lt/registracija")
        self.driver.find_element(By.ID, 'UserName').send_keys(f"Jurgio pyragai{random.randint(1000, 9999)}")
        self.driver.find_element(By.ID, 'Email').send_keys(f'ne@tavo{random.randint(1000, 9999)}.lt')
        self.driver.find_element(By.ID, 'Password').send_keys('Aasrgt1!')
        self.driver.find_element(By.ID, 'Password2').send_keys('Aasrgt1!123')
        self.driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()

        actual_text = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/form/fieldset/table/tbody/tr[8]/td[2]/span').text
        expected_text = 'Nesutampa slaptažodžiai. Pakartokite.'

        self.assertEqual(actual_text, expected_text)

    def test_reg_form_2_letters_username(self):
        print("tikiuosi, kad NEleis sukurti")

    def test_reg_form_3_letters_username(self):
        print("tikiuosi, kad leis sukurti")

    def test_reg_form_20_letters_username(self):
        print("tikiuosi, kad leis sukurti")

    def test_reg_form_21_letters_username(self):
        print("tikiuosi, kad NEleis sukurti")

    def tearDown(self):
        self.driver.quit()

    def acceptCookies(self):
        self.driver.get("https://elenta.lt")
        self.driver.find_element(By.CLASS_NAME, 'fc-cta-consent').click()
