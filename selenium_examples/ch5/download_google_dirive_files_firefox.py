#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-20
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile(r'C:\Users\acer\AppData\Roaming\Mozilla\Firefox\Profiles\ar8m1pr8.default')
driver = webdriver.Firefox(fp)
driver.get("https://smtebooks.net/book/14870/mastering-python-networking-security-pdf")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(18)
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_id("download").click()
driver.find_element_by_css_selector("i.fa.fa-cloud-download").click()

input('Press ENTER to close the automated browser')
driver.quit()

