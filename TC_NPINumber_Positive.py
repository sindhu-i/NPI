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
#   3. Enter valid NPI number
#   4. Click on search
#   5. Verify whether data is displayed or no data

driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Enter the url
driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")
# Maximize the window
driver.maximize_window()
time.sleep(5)
# Click on toggle button(NPI Search level)
driver.find_element(By.XPATH, "//button[@role='switch']").click()
time.sleep(2)
# Enter valid NPI Number

driver.find_element(By.XPATH, "//input[@placeholder='Enter NPI Number']").send_keys("1861477739")
# Click on search
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[2]/button").click()
time.sleep(5)
# Capture grid columns
NPISearch_columns = driver.find_elements(By.XPATH, "//*[@class = 'ant-table-thead']")
for item in NPISearch_columns:
    print(item.text)
    print(type(item.text))
    time.sleep(2)
# converting above to list
NPISearch_Grid = (item.text).split()
print(NPISearch_Grid)
if NPISearch_Grid == ['NPI', 'Presentation', 'Name', 'Provider', 'Type', 'Specialty', 'Name', 'Networks', 'Utilization', 'Score']:
    print('TestCase: Search By NPI number functionality with valid data is passed')
else:
     print('TestCase: Search By NPI number functionality with valid data is failed')
