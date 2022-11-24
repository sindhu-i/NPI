import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Test Steps
# 1. Open browser
# 2. Enter url
# 3. Click on open view button
# 4. Click on load original view
# 5. Verify original view loaded
driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")

driver.maximize_window()
time.sleep(10)
# # click on open view button
# driver.find_element(By.XPATH, "//span[@title='Open View']").click()
# time.sleep(2)
# # click on load original view
# driver.find_element(By.XPATH, "//div[@role='document']//div//div//div//button[@type='button']").click()
# time.sleep(5)
# original_view = driver.find_element(By.XPATH, "//*[text() = 'Original View']")
# if original_view.text == 'Original View':
#     print("Testcase passed")
# else:
#     print("Testcase failed")
# time.sleep(5)


# for index in range(1, len(list_view)-1):
#     print(list_view[index].text)

driver.close()