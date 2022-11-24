import time

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
time.sleep(10)
# Verifying Zipcode/Geogrpahy fields
# click on Geography button
driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper']").click()
time.sleep(5)
Geo = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[9]/div[2]/label[2]/span[2]").text
Geo1 = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[8]/div[1]").text
print(Geo)
print(Geo1)
time.sleep(2)
if Geo == Geo1:
    print('TestCase passed')
    # click on Zipcode button
    driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper']").click()
    time.sleep(2)
    Z = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[9]/div[2]/label[1]/span[2]").text
    print(Z)
    Z1 = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[8]/div[1]").text
    print(Z1)
    if Z == Z1:
        print("TestCase passed")
    else:
        print("TestCase failed")

else:
    print('TestCase failed')
