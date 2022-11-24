import random
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
time.sleep(20)
# TestSteps
# 1. Open the browser
# 2. Enter url
# 3. Verify if NPI type is Hospital, then Firstname and last name fields must be disabled
# 4. Verify if NPI type is PCP or Specialist, then Organization name field must be disabled
#
# # Get NPI type selected value
# Npi = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]").text
# time.sleep(2)
# print(Npi)
# time.sleep(2)
# if Npi == 'Hospital':
#     # Verifying Firstname and last name fields are disabled
#     #F_name = driver.find_element(By.CSS_SELECTOR,"body div[id='root'] div[class='content_content__A0Ufa'] div[class='ant-row content_search-filter-wrapper__ZGGmI'] div[class='content_show__l1TJz'] div[class='ant-col ant-col-24 content_filter-container__PFeCY undefined content_show__l1TJz'] div:nth-child(3) span:nth-child(1)")
#     first_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter First Name']")
#     last_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter Last Name']")
#     # = driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/span[2]").is_enabled()
#     # print(L_name)
#     print(first_name.is_enabled())
#     print(last_name.is_enabled())
#     time.sleep(2)
#     # Org_name = driver.find_element(By.XPATH, "//span[@class='ant-input-affix-wrapper']").is_enabled()
#     org_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter Organization Name']")
#     print(org_name.is_enabled())
#     if (first_name.is_enabled()) and (last_name.is_enabled()) == 'False' and org_name.is_enabled() == 'True':
#         print("TestCase passed")
#     else:
#         print("Testcase failed")
#
#
# else:
#     print("Not hospital")
# # time.sleep(5)
# # Randomly selecting NPI type dropdown values
# # Taking all value info
# NPI= driver.find_elements(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div")
# # Clicking on NPI type dropdown
# driver.find_element(By.XPATH, "//body/div[@id='root']/div/div/div/div/div[1]/div[2]/div[1]").click()
# time.sleep(5)
# # Selecting PCP
# driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div").click()
# time.sleep(2)
# # Verifying the selected value in NPI type
# Npi1 = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]").text
# print(Npi1)
# time.sleep(5)
# if Npi1 == 'PCP':
#     print("testCase passed")
#     first_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter First Name']")
#     last_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter Last Name']")
#     org_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter Organization Name']")
#     print(first_name.is_enabled())
#     print(last_name.is_enabled())
#     print(org_name.is_enabled())
#     time.sleep(2)
#     if first_name.is_enabled() == True and last_name.is_enabled() == True and org_name.is_enabled() == False:
#         print("Passed")
#     else:
#         print("Failed")
# else:
#     print("Testcase failed")

# Clicking on NPI type dropdown
driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[3]/div/div[1]/div[2]").click()
time.sleep(2)
# Selecting Specialist
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div").click()
time.sleep(2)
# Verifying the selected value in NPI type
Npi2 = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]").text
print(Npi2)
#
# # Randomly selectin values from NPI dropdown
# # NPI= driver.find_elements(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div")
# # ran = random.choice(NPI)
# # ran.click()
# # time.sleep(5)
# Verifying Hospital affiliations dropdown when NPI type is Specialist
Aff_Hosp = driver.find_element(By.XPATH, "//span[normalize-space()='Affiliated to Hospital']")
time.sleep(3)
A = Aff_Hosp.is_displayed()

print(A)