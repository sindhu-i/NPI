import os
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
# Test steps for download functionality
# 1. Open browser
# 2. Enter url
# 3. Click download button
# 4. Verify download occured
driver.get("http://192.168.2.40:4040/npi-search/c2d731f6-907a-45ac-af28-eb7b355fa03e")
driver.maximize_window()
time.sleep(10)
# click on download button
driver.find_element(By.XPATH, "//span[@title='Download']").click()
time.sleep(2)
while not os.path.exists('C://Users//Sindhura//Downloads'):
if os.path.isfile('C://Users//Sindhura//Downloads//AZ_Maricopa_Hospital (5).xlsx'):
    print("File download is completed")
 else:
    print("File download is not completed")
