#coding=utf-8
from text_helper import *
from company_mapper import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

# add current directory to PATH so it can find driver
# export PATH=$PATH:$(pwd)
# path = os.getcwd() + '/chromedriver.exe'

driver = webdriver.Chrome()
print('You have 60 sec to login')

for name, url in company_mapper():
  print(name, url)
  driver.get(url)

  wait = WebDriverWait(driver, 60)

  try:
    elements = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, 'h3')))
    result = map(lambda element: element.text, elements)

    print(name, process(result))

  except TimeoutException as ex:
    print(driver.page_source.encode("utf-8"))

  # Switch to tab
  driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

