#coding=utf-8
import argparse
import sys
import csv
from number_helper import parse_dollar
from company_mapper import *
from stock import Transaction, Stock
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
  with open('performance.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Shares', 'Cost', 'Equity', 'Gain/Loss'])
  
  for symbol, url in mapper:
    driver.get(url)
    wait = WebDriverWait(driver, 60)

    try:
      elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, '_3znyYq5FdX98HAPHPumJG1')))
      history = map(lambda element: Transaction(element.text), elements)

      stock = Stock(symbol, history)
      stock.parse(args.exclude)
    except TimeoutException as ex:
      print("You don't have this stock")

    # Switch to tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

    # Get current equity
    driver.get('https://robinhood.com/stocks/' + symbol)
    wait = WebDriverWait(driver, 10)

    try:
      elements = wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, 'h2')))
      stock.equity = parse_dollar(elements[0].text)
    except TimeoutException as ex:
      print("You don't have this stock right now")

    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    
    print(stock.performance())

    with open('performance.csv', 'a') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow([stock.symbol, stock.shares, str(round(stock.total_cost, 2)), stock.equity, str(round(stock.gain_loss(), 2))])

def get_dividend(mapper):
  driver = webdriver.Chrome('./chromedriver')
  print('You have 60 sec to login')
  with open('dividend.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Dividend'])

  for symbol, url in mapper:
    driver.get(url)
    wait = WebDriverWait(driver, 60)

    try:
      elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, '_2dd7UBEjupbjwapwV9x2ys')))
      history = map(lambda element: element.text, elements)
      stock = Stock(symbol, history)

      stock.parse()

      print(stock.dividend())

      with open('dividend.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([stock.symbol, stock.dividend_gain])
    except TimeoutException as ex:
      print("You don't have this stock")

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Take a glance at how your robinhood performs')
  parser.add_argument('-c', '--custom', type=str,
                      help='use custom mapper, update custom_mapper.json with your portfolio')
  parser.add_argument('-d', '--dividend', action="store_true",
                      help='view your dividend gain by symbol')
  parser.add_argument('-e', '--exclude', action="store_true",
                      help='exclude dividend gain in performance')

  args = parser.parse_args()
  
  print('Start to read your portfolio...')

  if args.exclude:
    print('excluding dividend')

  default_path = './mapper/default_mapper.json'
  if args.dividend:
    print('view dividend gain')
    get_dividend(custom_mapper(args.custom or default_path))
  else:
    run(custom_mapper(args.custom or default_path))
