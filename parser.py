#coding=utf-8
import argparse
import sys
from text_helper import *
from company_mapper import *
from summary import Summary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

# add current directory to PATH so it can find driver
# export PATH=$PATH:$(pwd)
# path = os.getcwd() + '/chromedriver.exe'

def run(mapper):
  driver = webdriver.Chrome()
  print('You have 60 sec to login')
  
  for name, url in mapper:
    driver.get(url)
    summary = Summary(name)
    
    wait = WebDriverWait(driver, 60)

    try:
      elements = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, 'h3')))
      result = map(lambda element: element.text, elements)
      
      summary.history, summary.total_cost = process(result, args.exclude)
    except TimeoutException as ex:
      print("You don't have this stock")

    # Switch to tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

    # Get current equity
    driver.get('https://robinhood.com/stocks/' + name)
    wait = WebDriverWait(driver, 10)

    try:
      elements = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, 'h2')))
      summary.equity = parse_dollar(elements[0].text)
    except TimeoutException as ex:
      print("You don't have this stock right now")

    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    
    print(summary)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Take a glance at how your robinhood performs')
  parser.add_argument('-c', '--custom', action="store_true",
                      help='use custom mapper, pdate custom_mapper.json with your portfolio')
  parser.add_argument('-e', '--exclude', action="store_true",
                      help='exclude dividend gain in performance')

  args = parser.parse_args()

  if args.custom:
    print('Start to read your portfolio...')
    if args.exclude:
      print('excluding dividend')
    run(custom_mapper())
  else:
    run(default_mapper())
