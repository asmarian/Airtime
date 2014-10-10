# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ft1AdminLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ft1_admin_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("testadmin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("testadmin")
        driver.find_element_by_id("submit").click()
        current_user = driver.find_element_by_class_name("name")
        self.assertEqual(current_user.text, 'testadmin')
        driver.find_element_by_class_name("name").click()
        username = driver.find_element_by_id("cu_login")
        username_value = username.get_attribute("value")
        firstname = driver.find_element_by_id("cu_first_name")
        firstname_value = firstname.get_attribute("value")
        lastname = driver.find_element_by_id("cu_last_name")
        lastname_value = lastname.get_attribute("value")
        email = driver.find_element_by_id("cu_email")
        email_value = email.get_attribute("value")
        phone = driver.find_element_by_id("cu_cell_phone")
        phone_value = phone.get_attribute("value")

        self.assertEqual(username_value, 'testadmin')
        self.assertEqual(firstname_value, 'testadmin_name')
        self.assertEqual(lastname_value, 'testadmin_lastname')
        self.assertEqual(email_value, 'testadmin@email.com')
        self.assertEqual(phone_value, '1234567890')

        #check for top menu now playing, calendar, add media, library, system, help, calendar
        m1=driver.find_element_by_xpath("/html/body/div[1]/ul/li[1]/a/span")
        self.assertEqual(m1.text, 'NOW PLAYING')
        m2=driver.find_element_by_xpath("/html/body/div[1]/ul/li[2]/a/span")
        self.assertEqual(m1.text, 'ADD MEDIA')
        m3=driver.find_element_by_xpath("/html/body/div[1]/ul/li[3]/a/span")
        self.assertEqual(m1.text, 'LIBRARY')
        m4=driver.find_element_by_xpath("/html/body/div[1]/ul/li[4]/a/span")
        self.assertEqual(m1.text, 'CALENDAR')
        m6=driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a/span")
        self.assertEqual(m1.text, 'SYSTEM')
        m5=driver.find_element_by_xpath("/html/body/div[1]/ul/li[6]/a/span")
        self.assertEqual(m1.text, 'HISTORY')
        m6=driver.find_element_by_xpath("/html/body/div[1]/ul/li[7]/a/span")
        self.assertEqual(m1.text, 'HELP')


        driver.find_element_by_link_text("Logout").click()


    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
