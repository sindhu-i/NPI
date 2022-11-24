import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
# 1. Open browser
# 2. Enter url
# 3. Click on clear button
# 4. Verify all fields are empty
# 5. Click on search button
# 6. Verify mandatory fields must display error message

driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(options.add_experimental_option()=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(executable_path= "C://Users//Sindhura//Desktop//Work//Testing//Automation//chromedriver_win32 (1)//chromedriver.exe")

driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")

driver.maximize_window()
time.sleep(5)

# click on clear button

driver.find_element(by=By.XPATH, value = "//button[@class='ant-btn']").click()
time.sleep(10)

# checking if NPI type field is empty
# copying NPI, State, County, Zipcode fields attribute
Npi = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]").text
time.sleep(2)
State = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[6]/div[2]/div[1]").text
time.sleep(2)
County = driver.find_element(By.XPATH, "//span[normalize-space()='Select County']").text
time.sleep(2)
Zipcode = driver.find_element(By.XPATH, "//div[8]//div[2]//div[1]").text
time.sleep(5)
print(Npi)
print(State)
print(County)
print(Zipcode)


if Npi == 'Select NPI Type' and State == 'Select State' and County == 'Select County' and Zipcode == 'Select Zipcode':
     print("Fields are empty")
     # if State == 'Select State':
     #     print("State field is empty")
     #     if County == 'Select County':
     #         print("County field is empty")
     #         if Zipcode == 'Select Zipcode':
     #             print("Zipcode is empty")
     #         else:
     #             print("Zipcode is not empty")
     time.sleep(2)
     #
     driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/button[1]").click()
     time.sleep(5)
     NPI_empty = driver.find_element(By.XPATH, "//p[normalize-space()='Please Select the NPI Type!']").text
     State_empty = driver.find_element(By.XPATH, "//p[normalize-space()='Please Select the State!']").text
     County_empty = driver.find_element(By.XPATH, "//p[normalize-space()='Please Select the County!']").text
     Zipcode_empty = driver.find_element(By.XPATH, "//p[normalize-space()='Please Select the Zipcode!']").text
     Blank_Grid = driver.find_element(By.XPATH, "//span[normalize-space()='Please Search Something...']").text
     time.sleep(5)
     print(NPI_empty)
     print(State_empty)
     print(County_empty)
     print(Zipcode_empty)
     print(Blank_Grid)
     if NPI_empty == 'Please Select the NPI Type!' and State_empty == 'Please Select the State!' and County_empty == 'Please Select the County!'and  Zipcode_empty == 'Please Select the Zipcode!' and Blank_Grid == 'Please Search Something...':
         print('TestCase_step2 passed')

     else:
         print('TestCase_step1 failed')
else:
     print("Fields are not empty")
     time.sleep(10)
# Verifying Zipcode/Geogrpahy fields
Z = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[9]/div[2]/label[1]/span[2]").text
print(Z)


