#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = "https://drive.google.com"
fp = webdriver.FirefoxProfile(r'C:\Users\acer\AppData\Local\Mozilla\Firefox\Profiles\ar8m1pr8.default')
driver = webdriver.Firefox(fp)
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
element = driver.find_element_by_class_name("a-s-Xc-ag-fa-Te")
element.click()
actions = ActionChains(self.driver)
actions.send_keys(Keys.DELETE)
actions.perform()

input('Press ENTER to close the automated browser')
driver.quit()

