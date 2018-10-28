#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://guidebook.seleniumacademy.com/Selectable.html")
driver.implicitly_wait(30)
driver.maximize_window()
one = driver.find_element_by_name('one')
two = driver.find_element_by_name('two')
three = driver.find_element_by_name('three')
ActionChains(driver).key_down(Keys.CONTROL).click(one).click(two).click(three).key_up(Keys.CONTROL).perform()
input('Press ENTER to close the automated browser')
driver.quit()

