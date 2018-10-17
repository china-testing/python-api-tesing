#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-16

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://httpbin.org/forms/post')
custname = browser.find_element_by_name("custname")
custname.clear()
custname.send_keys("python测试开发")

time.sleep(2)
for size_element in browser.find_elements_by_name("size"):  
    if size_element.get_attribute('value') == 'medium':
        size_element.click()
   
time.sleep(2)        
for topping in browser.find_elements_by_name('topping'):
    if topping.get_attribute('value') in ['bacon', 'cheese']:
        topping.click()
    
time.sleep(2)           
browser.find_element_by_tag_name('form').submit()