#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile(r'C:\Users\acer\AppData\Roaming\Mozilla\Firefox\Profiles\ar8m1pr8.default')
driver = webdriver.Firefox(fp)
driver.get("https://drive.google.com")
driver.implicitly_wait(20)
driver.maximize_window()

elements = driver.find_elements_by_xpath("//div[3]/span")
while elements:
    ActionChains(driver).click(elements[0]).send_keys(Keys.DELETE).perform()
    elements = driver.find_elements_by_xpath("//div[3]/span")
    
input('Press ENTER to close the automated browser')
driver.quit()

