import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)

# Testcase for search by NPI number functionality with valid data(NPI number)
# 1. Open the browser
#   2. Enter url
#   3. Enter invalid NPI number
#   4. Click on search
#   5. Verify NPI number search field is displaying error message

driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Enter the url
driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")
# Maximize the window
driver.maximize_window()
time.sleep(20)
# Click on toggle button(NPI Search level)
driver.find_element(By.XPATH, "//button[@role='switch']").click()
time.sleep(2)
# Enter invalid NPI Number
driver.find_element(By.XPATH, "//input[@placeholder='Enter NPI Number']").send_keys("18614777")
# Click on search
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[2]/button").click()
time.sleep(2)
# Capture error message
NPI_errormsg = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div/p")
print(NPI_errormsg.text)
Grid_errormsg = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[3]/div[2]/span")
print(Grid_errormsg.text)
time.sleep(5)
# click on clear button
driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click()
time.sleep(2)
# Click on search button
driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
time.sleep(2)
# Capture error message
NPI_errormsg2 = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div/p")
print(NPI_errormsg2.text)
Grid_errormsg2 = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[3]/div[2]/span")
print(Grid_errormsg2.text)

time.sleep(2)

if (NPI_errormsg.text) and (NPI_errormsg2.text) == 'Please enter valid NPI Number!' and (Grid_errormsg.text) and (Grid_errormsg2.text)=='Please Search Something...':
    print('TestCase: Search by NPI number with invalid data passed')
else:
    print('TestCase: Search by NPI number with invalid data failed')
time.sleep(5)
driver.close()
