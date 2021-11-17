import csv
import time
from selenium import webdriver
from difflib import SequenceMatcher
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

s = '/Users/prashampatel/Desktop/projects/autofbthisisit/chromedriver'

options = Options()
options.headless = True
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(s, options=options)

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


use_cat = ''
fields = ['Title', 'Category1', 'Category2', 'Category3', 'Category4', 'Description']
rows = []

def get_product_title_description(prod_url):
    driver.get(prod_url)
    try:
        title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    except NoSuchElementException:
        title = 'REMOVE'
    # price = driver.find_element(By.ID, 'priceblock_ourprice').text # FIX THIS
    try:
        description = driver.find_element(By.XPATH, '//*[@id="feature-bullets"]/ul').text
    except NoSuchElementException:
        description = ''
    breadcrumb_cats = [cats.text.split(sep='\n') for cats in driver.find_elements(By.CSS_SELECTOR, '#wayfinding'
                                                                                                   '-breadcrumbs'
                                                                                                   '_feature_div > ul')]
    try:
        category1 = breadcrumb_cats[0][0]
        category2 = breadcrumb_cats[0][2]
        category3 = breadcrumb_cats[0][4]
        category4 = breadcrumb_cats[0][6]
    except IndexError:
        category1 = ''
        category2 = ''
        category3 = ''
        category4 = ''
    rows.append([str(title), str(category1),str(category2), str(category3), str(category4), str(description)])
    with open('product_data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


with open('products.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    i = 0
    for row in csv_reader:
        for i in range(len(row)):
            get_product_title_description(row[i])
            i += 1
            print(i)

