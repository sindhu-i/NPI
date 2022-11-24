import string
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Test steps for saving a view
# 1. Open browser
# 2. Enter url
# 3. Click on save view button
# 4. Enter valid name
# 5. Click on save

driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")
driver.maximize_window()
time.sleep(10)
# # Click on save view button
# driver.find_element(By.XPATH, "//span[@title='Save As View']").click()
# time.sleep(2)
# # Enter random value
# view_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter the view name']")
# randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
# view_name.send_keys(randstring)
# view_name1 = driver.find_element(By.XPATH, "//input[@placeholder='Enter the view name']").get_attribute('value')
# print(view_name1)
# # Click on save button
# driver.find_element(By.XPATH, "//div[@role='document']//div//div//button[@type='button']").click()
# time.sleep(2)
# # validate saved view notification
# notification = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]").text
# print(notification)
# if 'created' in notification:
#     print('1st check passed')
#
# else:
#     print('1st check failed')
# time.sleep(2)
# click on open view button
driver.find_element(By.XPATH, "//span[@title='Open View']").click()
time.sleep(3)
# click on 'Select the view' dropdown
driver.find_element(By.XPATH,"//div[@role='document']//div//div//div//div").click()
# Capturing all saved views from the list
items = driver.find_elements(By.XPATH,'//*[@class ="ant-select-dropdown ant-select-dropdown-placement-bottomLeft  ant-select-dropdown-hidden"]')
# items = driver.find_elements(By.XPATH, "//*[@class='rc-virtual-list-holder-inner']")
# items = driver.find_elements(By.XPATH, "//*[@class='rc-virtual-list-holder and @class = 'rc-virtual-list-holder-inner']")
# items = driver.find_elements(By.XPATH, "rc-virtual-list-holder-inner")
time.sleep(2)
for item in items:
    print(item.text)