#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://guidebook.seleniumacademy.com/Selectable.html")
driver.implicitly_wait(30)
driver.maximize_window()
one= driver.find_element_by_name('one')
print(one.location)
print(one.size)
six = driver.find_element_by_name('six')
print(six.location)
print(six.size)
actions = ActionChains(driver)
actions.move_by_offset(one.size['width'] + one.location['x'],
                       one.size['height'] + one.location['y']).click().perform()
input('Press ENTER to close the automated browser')
driver.quit()

