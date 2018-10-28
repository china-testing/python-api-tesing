#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-18

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class at_least_n_elements_found(object):
    def __init__(self, locator, n):
        self.locator = locator
        self.n = n
        
    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) >= self.n:
            return elements
        else:
            return False
        
url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome()
driver.get(url)
# Use an implicit wait for cases where we don't use an explicit one
driver.implicitly_wait(10)
div_element = driver.find_element_by_class_name('infinite-scroll')
quotes_locator = (By.CSS_SELECTOR, ".quote:not(.decode)")

nr_quotes = 0
while True:
    
    # Scroll down to the bottom, now using action (chains)
    action_chain = ActionChains(driver)
    # Move to our quotes block
    action_chain.move_to_element(div_element)
    # Click it to give it focus
    action_chain.click()
    # Press the page down key about 10 ten times
    action_chain.send_keys([Keys.PAGE_DOWN for i in range(10)])
    # Do these actions
    action_chain.perform()
    
    # Try to fetch at least nr_quotes+1 quotes
    try:
        all_quotes = WebDriverWait(driver, 3).until(
            at_least_n_elements_found(quotes_locator, nr_quotes + 1))
    except TimeoutException as ex:
        # No new quotes found within 3 seconds, assume this is all there is
        print("... done!")
        break
    
    # Otherwise, update the quote counter
    nr_quotes = len(all_quotes)
    print("... now seeing", nr_quotes, "quotes")
    
# all_quotes will contain all the quote elements
print(len(all_quotes), 'quotes found\n')
for quote in all_quotes:
    print(quote.text)
input('Press ENTER to close the automated browser')
driver.quit()
