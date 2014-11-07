__author__ = 'nareg'

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, sys, psycopg2
import selenium.webdriver.common.alert
from settings import UPLOAD_MP3
from funtion_box import *
from datetime import datetime
from selenium import webdriver



# function for setting up page, webdriver with firefox and loging in with admin
def setUpAll(self, username, password):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(5)
    self.base_url = BASIC_URL
    self.verificationErrors = []
    self.accept_next_alert = True
    driver = self.driver
    driver.get(self.base_url + "/login")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(tr_word(username))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(password))
    driver.find_element_by_id("submit").click()


def login(self, username, password):
    driver = self.driver
    driver.get(self.base_url + "/login")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(tr_word(username))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(password))
    driver.find_element_by_id("submit").click()


def change_time_zone(self):
    driver = self.driver
    driver.find_element_by_id("current-user").click()
    driver.find_element_by_css_selector("option[value=\"America/Toronto\"]").click()
    driver.find_element_by_id("cu_save_user").click()


def add_file(self, filename):
    driver = self.driver
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(filename)


def upload_file(self, file_location, filename):
    driver = self.driver
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(file_location)
    time.sleep(5)
    driver.find_element_by_link_text("Start upload").click()
    time.sleep(5)
    trackid = get_track_id(filename)
    return trackid


def my_date_time():
    d = datetime.datetime.now()
    hour = d.hour
    minutes = d.minute + 2
    ingre = str(d.hour) + ":" + str(minutes)
    localtime = time.localtime()
    timstr = time.strftime("%Y-%m-%d", localtime)
    return timstr, ingre


def go_to_folder(self, foldername):
    driver = self.driver
    driver.find_element_by_link_text(foldername).click()


def go_to_subfolder(self, foldername, subfolder):
    driver = self.driver
    driver.find_element_by_link_text(foldername).click()
    driver.find_element_by_link_text(subfolder).click()


def handle_alert(self):
    driver = self.driver
    alert = driver.switch_to.alert
    alert.accept()


def create_guest(self):
    driver = self.driver
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(tr_word(GUEST_LOGIN))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(GUEST_PASS))
    driver.find_element_by_id("passwordVerify").clear()
    driver.find_element_by_id("passwordVerify").send_keys(tr_word(GUEST_PASS))
    driver.find_element_by_id("first_name").clear()
    driver.find_element_by_id("first_name").send_keys(tr_word(GUEST_NAME))
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys(tr_word(GUEST_LASTNAME))
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(tr_word(GUEST_EMAIL))
    driver.find_element_by_id("cell_phone").clear()
    driver.find_element_by_id("cell_phone").send_keys(PHONE)
    type = driver.find_element_by_id("type")
    guest = driver.find_element_by_id("user-type-G").click()
    ActionChains(driver).move_to_element(type).double_click(guest)
    time.sleep(3)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    time.sleep(3)


def create_dj(self):
    driver = self.driver
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(tr_word(DJ_LOGIN))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(DJ_PASS))
    driver.find_element_by_id("passwordVerify").clear()
    driver.find_element_by_id("passwordVerify").send_keys(tr_word(DJ_PASS))
    driver.find_element_by_id("first_name").clear()
    driver.find_element_by_id("first_name").send_keys(tr_word(DJ_NAME))
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys(tr_word(DJ_LASTNAME))
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(tr_word(DJ_EMAIL))
    driver.find_element_by_id("cell_phone").clear()
    driver.find_element_by_id("cell_phone").send_keys(PHONE)
    type = driver.find_element_by_id("type")
    guest = driver.find_element_by_id("user-type-H").click()
    ActionChains(driver).move_to_element(type).double_click(guest)
    time.sleep(3)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    time.sleep(3)


def create_pr(self):
    driver = self.driver
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(tr_word(PR_LOGIN))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(PR_PASS))
    driver.find_element_by_id("passwordVerify").clear()
    driver.find_element_by_id("passwordVerify").send_keys(tr_word(PR_PASS))
    driver.find_element_by_id("first_name").clear()
    driver.find_element_by_id("first_name").send_keys(tr_word(PR_NAME))
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys(tr_word(PR_LASTNAME))
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(tr_word(PR_EMAIL))
    driver.find_element_by_id("cell_phone").clear()
    driver.find_element_by_id("cell_phone").send_keys(PHONE)
    type = driver.find_element_by_id("type")
    guest = driver.find_element_by_id("user-type-P").click()
    ActionChains(driver).move_to_element(type).double_click(guest)
    time.sleep(3)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    time.sleep(3)


def create_admin(self):
    driver = self.driver
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(tr_word(TADMIN_LOGIN))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(tr_word(TADMIN_PASS))
    driver.find_element_by_id("passwordVerify").clear()
    driver.find_element_by_id("passwordVerify").send_keys(tr_word(TADMIN_PASS))
    driver.find_element_by_id("first_name").clear()
    driver.find_element_by_id("first_name").send_keys(tr_word(TADMIN_NAME))
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys(tr_word(TADMIN_LASTNAME))
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(tr_word(TADMIN_EMAIL))
    driver.find_element_by_id("cell_phone").clear()
    driver.find_element_by_id("cell_phone").send_keys(PHONE)
    type = driver.find_element_by_id("type")
    guest = driver.find_element_by_id("user-type-A").click()
    ActionChains(driver).move_to_element(type).double_click(guest)
    time.sleep(3)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    time.sleep(3)


def create_show(self, show_name):
    driver = self.driver
    go_to_folder(self, "CALENDAR")
    driver.find_element_by_class_name("add-button").click()
    driver.find_element_by_id("add_show_name").clear()
    driver.find_element_by_id("add_show_name").send_keys(tr_word(show_name))
    driver.find_element_by_xpath("//div[@id='schedule-add-show']/h3[2]/span").click()
    # date, hour = my_date_time()
    driver.find_element_by_id("add_show_start_time").clear()
    driver.find_element_by_id("add_show_start_time").send_keys("22:00")
    driver.find_element_by_id("add_show_end_time").clear()
    driver.find_element_by_id("add_show_end_time").send_keys("23:00")
    driver.find_element_by_class_name("ui-button-text").click()


def add_content_to_show(self, show_id, media_id):
    driver = self.driver
    go_to_folder(self, "CALENDAR")
    driver.find_element_by_xpath("//div[@data-show-id='%s']" % show_id).click()
    driver.find_element_by_class_name("icon-add-remove-content").click()
    time.sleep(5)
    media = driver.find_element_by_id(utilize_id(media_id))
    ActionChains(driver).double_click(media).perform()
    driver.find_element_by_class_name("ui-dialog-buttonset").click()


def check_existence_by_id(self, path):
    driver = self.driver
    try:
        driver.find_element_by_id(path)
    except NoSuchElementException:
        return False
    return True






