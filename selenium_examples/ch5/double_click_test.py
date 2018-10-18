#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-10-18

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class DoubleClickTest (unittest.TestCase):

    URL = 'http://api.jquery.com/dblclick/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def test_double_click(self):
        driver = self.driver
        frame = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame)
        box = driver.find_element_by_tag_name('div')

        # verify color is Blue
        self.assertEqual('rgba(0, 0, 255, 1)',
                         box.value_of_css_property('background-color'))

        ActionChains(driver).move_to_element(
            driver.find_element_by_tag_name('body')).perform()
        ActionChains(driver).double_click(box).perform()

        # verify Color is Yellow
        self.assertEqual('rgba(255, 255, 0, 1)',
                         box.value_of_css_property('background-color'))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
