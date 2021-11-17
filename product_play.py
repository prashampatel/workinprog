from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains


s = '/Users/prashampatel/Desktop/projects/autofbthisisit/chromedriver'
prod_link = 'https://www.amazon.com/Ring-Size-Adjuster-Loose-Rings/dp/B0757JLTY7/ref=zg_bs_arts-crafts_10?_encoding=UTF8&psc=1&refRID=NW76QASRHVW25TZG03RW'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(s, options=options)

driver.get(prod_link)

n = 0
for i in driver.find_elements(By.CSS_SELECTOR, '#altImages .imageThumbnail'):
    n += 1
    hover = ActionChains(driver).move_to_element(i)
    hover.perform()
    img_src = driver.find_element(By.CSS_SELECTOR,'.image.item.maintain-height.selected img').get_attribute('src')
    urllib.request.urlretrieve(img_src, f"current_product/{n}.png")

driver.close()


