# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Functional tests

class TestBlazedemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://blazedemo.com/"
    
    def test_title(self):
        driver = self.driver
        driver.get("http://www.blazedemo.com")
        assert "Simple Flights" in driver.title
        driver.close()
        
    def test_contents(self):
        driver = self.driver
        driver.get("http://www.blazedemo.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("departure")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
        
    def test_defaults(self):
        driver = self.driver
        driver.get("http://www.blazedemo.com")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("(//input[@value='Choose This Flight'])[1]").click()
        driver.implicitly_wait(1)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.implicitly_wait(30)
        driver.close()
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
