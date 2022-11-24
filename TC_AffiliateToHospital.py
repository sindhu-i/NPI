import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver. Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Enter the url
driver.get("http://192.168.2.40:4040/npi-search/1B6930D0-46B8-40DC-867A-2099336E51D4")
# Maximize the window
driver.maximize_window()
time.sleep(20)
#Get NPI type selected value
Npi = driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]").text
time.sleep(2)
print(Npi)
time.sleep(2)
# if Npi == 'Hospital':
#    Aff_Hosp = driver.find_element(By.XPATH, "//span[normalize-space()='Affiliated to Hospital']").is_displayed()
#    if Aff_Hosp:
#            print("Element  displayed")
#    else:
#         print("Element not displayed")
#
# else:
#     print("Not hospital")

from selenium.common.exceptions import NoSuchElementException

try:
    Aff_Hosp = driver.find_element(By.XPATH, "//span[normalize-space()='Affiliated to Hospital']")

except NoSuchElementException:  #spelling error making this code not work as expected
    pass

    print('No Such element')





