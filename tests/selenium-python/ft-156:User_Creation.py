# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, sys
import psycopg2


class F156UserCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_ft156usercreation(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("submit").click()

        driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a/span").click()
        driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/ul/li[2]/a").click()


        #print users.text
        def find_word(text, search):

            result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
            if len(result)>0:
                return True
            else:
                return False
        #Create guest1

        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("guest1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("guest1")
        driver.find_element_by_id("passwordVerify").clear()
        driver.find_element_by_id("passwordVerify").send_keys("guest1")
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("guest1_name")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("guest1_lastname")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("guest1@email.com")
        driver.find_element_by_id("cell_phone").clear()
        driver.find_element_by_id("cell_phone").send_keys("1234567890")
        type=driver.find_element_by_id("type")
        guest=driver.find_element_by_id("user-type-G").click()
        ActionChains(driver).move_to_element(type).double_click(guest)
        time.sleep(3)
        save=driver.find_element_by_id("save_user")
        ActionChains(driver).double_click(save).perform()
        time.sleep(3)

        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, "guest1"))
        self.assertTrue(find_word(users.text, "guest1_name"))
        self.assertTrue(find_word(users.text, "guest1_lastname"))
        self.assertTrue(find_word(users.text, "Guest"))
         #Create DJ

        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("DJlogin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("djpassword")
        driver.find_element_by_id("passwordVerify").clear()
        driver.find_element_by_id("passwordVerify").send_keys("djpassword")
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("DJ_name")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("DJ_lastname")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("djmail@email.com")
        driver.find_element_by_id("cell_phone").clear()
        driver.find_element_by_id("cell_phone").send_keys("1234567890")
        type=driver.find_element_by_id("type")
        guest=driver.find_element_by_id("user-type-H").click()
        ActionChains(driver).move_to_element(type).double_click(guest)
        time.sleep(3)
        save=driver.find_element_by_id("save_user")
        ActionChains(driver).double_click(save).perform()
        time.sleep(3)

        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, "DJlogin"))
        self.assertTrue(find_word(users.text, "DJ_name"))
        self.assertTrue(find_word(users.text, "DJ_lastname"))
        self.assertTrue(find_word(users.text, "DJ"))
         #Create Program Manager

        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("progman")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("progman")
        driver.find_element_by_id("passwordVerify").clear()
        driver.find_element_by_id("passwordVerify").send_keys("progman")
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("progman_name")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("progman_lastname")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("progman@email.com")
        driver.find_element_by_id("cell_phone").clear()
        driver.find_element_by_id("cell_phone").send_keys("1234567890")
        type=driver.find_element_by_id("type")
        guest=driver.find_element_by_id("user-type-P").click()
        ActionChains(driver).move_to_element(type).double_click(guest)
        time.sleep(3)
        save=driver.find_element_by_id("save_user")
        ActionChains(driver).double_click(save).perform()
        time.sleep(3)

        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, "progman"))
        self.assertTrue(find_word(users.text, "progman_name"))
        self.assertTrue(find_word(users.text, "progman_lastname"))
        self.assertTrue(find_word(users.text, "Program Manager"))
         #Create Admin

        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("testadmin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("testadmin")
        driver.find_element_by_id("passwordVerify").clear()
        driver.find_element_by_id("passwordVerify").send_keys("testadmin")
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("testadmin_name")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("testadmin_lastname")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("testadmin@email.com")
        driver.find_element_by_id("cell_phone").clear()
        driver.find_element_by_id("cell_phone").send_keys("1234567890")
        type=driver.find_element_by_id("type")
        guest=driver.find_element_by_id("user-type-A").click()
        ActionChains(driver).move_to_element(type).double_click(guest)
        time.sleep(3)
        save=driver.find_element_by_id("save_user")
        ActionChains(driver).double_click(save).perform()
        time.sleep(3)

        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, "testadmin"))
        self.assertTrue(find_word(users.text, "testadmin_name"))
        self.assertTrue(find_word(users.text, "testadmin_lastname"))
        self.assertTrue(find_word(users.text, "Admin"))

        conn = psycopg2.connect(database="airtime", user="airtime", password="airtime", host="127.0.0.1", port="5432")

        cur = conn.cursor()

        #cur.execute("DELETE FROM cc_subjs WHERE login='guest1';")
        #cur.execute("DELETE FROM cc_subjs WHERE login='DJlogin';")
        #cur.execute("DELETE FROM cc_subjs WHERE login='progman';")
        #cur.execute("DELETE FROM cc_subjs WHERE login='testadmin';")


        conn.commit()
        conn.close()


        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
