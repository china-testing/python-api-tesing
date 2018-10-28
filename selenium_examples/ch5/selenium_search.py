#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
 
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get('http://example.webscraping.com/places/default/search')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '300';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
print(len(countries))
print(countries)

driver.close()
