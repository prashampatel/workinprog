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
# options.headless = True
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(s, options=options)
amz_link = 'https://www.amazon.com/'

arts_crafts = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[6]/a'
automotive = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[8]/a'
beauty = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[10]/a'
camera = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[12]/a'
phone_access = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[14]/a'
clothing = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[15]/a'
computers_access = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[17]/a'
electronics = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[20]/a'
health_household = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[25]/a'
home_kitchen = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[26]/a'
kitchen_dining = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[29]/a'
office = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[33]/a'
patio_lawn = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[34]/a'
sports_outdoors = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[37]/a'
tools_improvement = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[39]/a'
toys_games = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[40]/a'
video_games = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/ul/ul/li[41]/a'
categories = [arts_crafts, automotive, beauty, camera, phone_access, clothing, computers_access, electronics,
               health_household, home_kitchen, kitchen_dining, office, patio_lawn, sports_outdoors, tools_improvement,
               toys_games, video_games]
driver.get(amz_link)
time.sleep(3)
bs = driver.find_element(By.PARTIAL_LINK_TEXT, 'Best Seller')
ac = ActionChains(driver)
bs.click()
product_xpaths_page1 = [f'/html/body/div[1]/div[3]/div/div/div[1]/div/ol/li[{n}]/span/div/span/a'
                  for n in range(1, 51)]
product_xpaths_page2 = [f'/html/body/div[1]/div[3]/div/div/div[1]/div/ol/li[{n}]/span/div/span/a'
                  for n in range(1, 51)]
product_urls = []

def get_urls(link):
    bs = driver.find_element(By.PARTIAL_LINK_TEXT, 'Best Seller')
    bs.click()
    find = driver.find_element(By.XPATH, link)
    find.click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    for path in product_xpaths_page1:
        try:
            prod = driver.find_element(By.XPATH, path)
            prod_url = prod.get_attribute('href')
            product_urls.append(prod_url)
        except NoSuchElementException:
            pass
    next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/div/ul/li[4]/a')
    next_page.click()
    for path in product_xpaths_page2:
        try:
            prod = driver.find_element(By.XPATH, path)
            prod_url = prod.get_attribute('href')
            product_urls.append(prod_url)
        except NoSuchElementException:
            pass


driver.get(amz_link)
time.sleep(3)

for link in categories:
    get_urls(link)

with open('products.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(product_urls)
