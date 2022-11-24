import string
import time
import random
# Test Case for Verifying columns of the Grid
# 1. Open the browser
# 2. Enter url
# 3. If NPI type is Hospital, verify the columns of the Grid
# 4. Change NPI type to PCP, Verify the columns of the Grid
# 5. Change NPI type to Specialist, Verify the columns of the Grid

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
# Capture NPI type dropdown selected value
Hospital = driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div[3]/div[1]/div[1]/div[2]")
print(Hospital.text)
time.sleep(5)
# Capture grid columns
H_columns= driver.find_elements(By.XPATH, "//*[@class = 'ant-table-thead']")
for item in H_columns:
    print(item.text)
    print(type(item.text))
time.sleep(2)
# converting above to list
HGrid = (item.text).split()
print(HGrid)
if Hospital.text == 'Hospital' and  HGrid==['NPI', 'Presentation', 'Name', 'Address', 'Specialty', 'Name', 'Networks', 'HGI', 'Rating', 'HCAHPS', 'Rating']:
    print('passed')
else:
     print('Failed')
time.sleep(5)
# Click on NPI type dropdown
driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div[3]/div[1]/div[1]/div[2]").click()
time.sleep(2)
# Select PCP
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div").click()
time.sleep(2)
# Click on Search button
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[2]/button").click()
time.sleep(5)
PCP = driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div[3]/div[1]/div[1]/div[2]")
# Capture grid columns
PCP_columns= driver.find_elements(By.XPATH, "//*[@class = 'ant-table-thead']")
for item in PCP_columns:
    print(item.text)
    print(type(item.text))
time.sleep(2)
# converting above to list
PCP_Grid = (item.text).split()
print(PCP_Grid)
if PCP.text == 'PCP' and PCP_Grid == ['NPI', 'Presentation', 'Name', 'Provider', 'Type', 'Specialty', 'Name', 'Networks', 'Utilization', 'Score', 'Active', 'In', 'Preventive', 'Care']:
    print("2nd test passed")
    # Click on NPI type dropdown
    driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div[3]/div[1]/div[1]/div[2]").click()
    time.sleep(2)
    # Select Specialist
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div").click()
    time.sleep(2)
    # Click on Search button
    driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[2]/button").click()
    time.sleep(5)
    Specialist = driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div[3]/div[1]/div[1]/div[2]")
    # Capture grid columns
    Spec_columns = driver.find_elements(By.XPATH, "//*[@class = 'ant-table-thead']")
    for item in Spec_columns:
        print(item.text)
        print(type(item.text))
    time.sleep(2)
    # converting above to list
    Spec_Grid = (item.text).split()
    print(Spec_Grid)
    if Specialist.text == 'Specialist' and Spec_Grid == ['NPI', 'Presentation', 'Name', 'Provider', 'Type', 'Specialty', 'Name', 'Networks', 'Utilization', 'Score']:
         print("3rd test passed")
        # Click on toggle button(NPI Search level)
         driver.find_element(By.XPATH, "//button[@role='switch']").click()
         time.sleep(2)
         # Enter valid NPI Number
         driver.find_element(By.XPATH, "//input[@placeholder='Enter NPI Number']").send_keys("1861477739")
         time.sleep(2)
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
         if NPISearch_Grid == Spec_Grid:
             print('4th test passed')
         else:
             print('4th test failed')
    else:
           print("3rd test failed")
else:
     print('2nd test failed')
driver.close()