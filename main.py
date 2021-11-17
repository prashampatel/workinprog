import os
import csv
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

mp = 'https://www.facebook.com/marketplace'
user = 'pp279@scarletmail.rutgers.edu'
pswd = 'A$ha0309'
s = os.getcwd() + '/chromedriver'


class Product:
    def __init__(self, title, price, description):
        self.title = title
        self.price = price
        # self.category = category
        self.condition = 'New'
        self.description = 'FREE SHIPPING ALWAYS\n' + description
        self.quantity = 5

    def __str__(self):
        return f'Title: {self.title}\nPrice: {self.price}\nDescription: {self.description}\nCondition: {self.condition}' \
               f'\nQuantity: {self.quantity}'


def create_product(prod_url):
    options2 = Options()
    options2.headless = True
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options2.add_experimental_option("prefs", prefs)
    driver2 = webdriver.Chrome(s, options=options2)
    driver2.get(prod_url)
    title = driver2.find_element(By.XPATH, '//*[@id="productTitle"]').text
    price = driver2.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]').text
    description = driver2.find_element(By.XPATH, '//*[@id="feature-bullets"]/ul').text
    return Product(title, price, description)


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(s, options=chrome_options)
ac = ActionChains(driver)
driver.get(mp)
time.sleep(2)
use_box = '//*[@id="login_form"]/div[2]/div[1]/label/input'
pas_box = '//*[@id="login_form"]/div[2]/div[2]/label/input'
user_box = driver.find_element(By.XPATH, use_box)
user_box.send_keys(user)
pswd_box = driver.find_element(By.XPATH, pas_box)
pswd_box.send_keys(pswd)
time.sleep(1)
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[1]/a')
pswd_box.send_keys(Keys.TAB)
pswd_box.send_keys(Keys.ENTER)
time.sleep(5)
driver.get('https://www.facebook.com/marketplace/create/item')
time.sleep(5)
image_input = driver.find_element(By.XPATH, "//input[@type='file']")
image_input.send_keys(os.getcwd() + '/current_product/1.png')
title_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div/label/div/div/input')
title_input.send_keys('I work')
price_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input')
price_input.send_keys('20')
ac.send_keys(Keys.TAB).perform()
ac.send_keys('Rings').perform()
ac.send_keys(Keys.TAB * 2).perform()
ac.send_keys(Keys.DOWN).perform()
ac.send_keys(Keys.TAB).perform()
ac.send_keys('this is description').perform()
ac.send_keys(Keys.TAB).perform()
ac.send_keys(10)