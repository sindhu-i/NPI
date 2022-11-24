import time
from random import random
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")

driver.maximize_window()
time.sleep(5)
# click on NPI type dropdown
driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div/div/div[1]/div[2]/div[1]").click()
time.sleep(4)
# Capturing all values from NPI dropdown
# items=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[6]/div/div")))
# item1 = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div")
item1 = driver.find_elements(By.XPATH, "//*[@class = 'rc-virtual-list-holder-inner']")
time.sleep(4)
for item in item1:
    print(item.text)
# randomIndex = int(random.random() * len(item1))
# # Getting the element present at the above index from the tuple
# randomItem = item1[randomIndex]
# randomItem.click()
#
# from random import randrange
# random_index = randrange(len(item1))
# item1[random_index].click()
