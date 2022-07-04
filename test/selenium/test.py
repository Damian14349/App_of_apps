import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import environ
from selenium.webdriver.common.by import By
 
application_URL = environ.get('APPLICATION_URL', 'http://localhost:5001/')
selenium_URL = environ.get('SELENIUM_URL', 'http://192.168.44.44:4444/wd/hub')

class Test()
    def setUp(self):
    self.driver = webdriver.Firefox()

    def test(self)
        driver = self.driver
        driver.get("APPLICATION_URL")
        elem = driver.find_element(By.NAME, "name")
        elem.send_keys("pycon")
        elem = driver.find_element(By.NAME, "animal")
        elem.send_keys("pycon")

if __name__ == "__main__":
    unittest.main()

