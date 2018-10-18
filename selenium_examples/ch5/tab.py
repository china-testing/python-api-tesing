#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-17
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://china-testing.github.io/")
driver.implicitly_wait(30)
driver.maximize_window()
element = driver.find_element_by_link_text('数据分析')
element.click()
time.sleep(3)
element = driver.find_element_by_link_text('python')
ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(
    Keys.CONTROL).perform()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.close() # 关闭当前TAB
time.sleep(3)
driver.quit()

