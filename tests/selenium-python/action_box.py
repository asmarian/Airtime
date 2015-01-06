__author__ = 'nareg'

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, re, sys, psycopg2
import selenium.webdriver.common.alert
from settings import UPLOAD_MP3
from funtion_box import *
from selenium import webdriver
from datetime import date, datetime, time, timedelta
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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


def change_time_zone(self, timezone):
    driver = self.driver
    driver.find_element_by_id("current-user").click()
    driver.find_element_by_css_selector("option[value=\"%s\"]" % timezone).click()
    driver.find_element_by_id("cu_save_user").click()


def add_file(self, filename):
    driver = self.driver
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(filename)


def upload_file(self, file_location, filename):
    driver = self.driver
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(file_location)
    self.driver.implicitly_wait(2)
    driver.find_element_by_link_text("Start upload").click()
    self.driver.implicitly_wait(2)
    # trackid = get_track_id(filename)
    #return trackid


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
    self.driver.implicitly_wait(2)
    save = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "save_user")))
    ActionChains(driver).double_click(save).perform()


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
    self.driver.implicitly_wait(5)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    self.driver.implicitly_wait(5)


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
    self.driver.implicitly_wait(2)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    self.driver.implicitly_wait(2)


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
    driver.implicitly_wait(2)
    save = driver.find_element_by_id("save_user")
    ActionChains(driver).double_click(save).perform()
    self.driver.implicitly_wait(2)


def create_show(self, show_name, show_start, show_end, repeat, link):
    driver = self.driver
    go_to_folder(self, "CALENDAR")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"add-button"))).click()
    driver.find_element_by_id("add_show_name").clear()
    driver.find_element_by_id("add_show_name").send_keys(tr_word(show_name))
    driver.find_element_by_xpath("//div[@id='schedule-add-show']/h3[2]/span").click()
    # date, hour = my_date_time()
    driver.find_element_by_id("add_show_start_time").clear()
    driver.find_element_by_id("add_show_start_time").send_keys(show_start)
    driver.find_element_by_id("add_show_end_time").clear()
    driver.find_element_by_id("add_show_end_time").send_keys(show_end)
    sleep(5)
    if repeat == "repeat":
        driver.find_element_by_id("add_show_repeats").click()
    if link == "link":
        driver.find_element_by_id("add_show_linked").click()
    driver.find_element_by_class_name("ui-button-text").click()
    driver.refresh()


def add_content_to_show_with_name(self, name, mp3name):
    driver = self.driver
    item1 = driver.find_element_by_xpath( "//span[@class='fc-event-title' and text()='%s']" % name)
    ActionChains(driver).click(item1).perform()
    sleep(5)
    driver.find_element_by_class_name( "icon-add-remove-content").click()
    media = driver.find_element_by_xpath("//td[@class='library_title' and text()='%s']" % mp3name)
    sleep(5)
    ActionChains(driver).double_click(media).perform()

    item2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn' and text()='Ok']")))
    ActionChains(driver).click(item2).perform()


def show_menu(self, show_name, action):
    driver = self.driver
    if action == "delete_instance":
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-event-title' and text()='%s']" % show_name )))
        ActionChains(driver).click(item).perform()
        header = driver.find_element_by_class_name("icon-delete").click()
        sleep(2)
        driver.find_element_by_xpath( "//li[contains(@class,'icon-delete')]//span[.='Delete This Instance']").click()


    elif action == "delete_instances":
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-event-title' and text()='%s']" % show_name )))
        ActionChains(driver).click(item).perform()
        header = driver.find_element_by_class_name("icon-delete").click()
        sleep(2)
        driver.find_element_by_xpath( "//li[contains(@class,'icon-delete')]//span[.='Delete This Instance and All Following']").click()

    elif action == "icon-overview":
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-event-title' and text()='%s']" % show_name )))
        ActionChains(driver).click(item).perform()
        driver.find_element_by_class_name('%s' % action).click()

    elif action == "icon-delete":
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-event-title' and text()='%s']" % show_name )))
        ActionChains(driver).click(item).perform()
        header = driver.find_element_by_class_name("icon-delete").click()

    elif action == "edit_instance":
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-event-title' and text()='%s']" % show_name )))
        ActionChains(driver).click(item).perform()
        header = driver.find_element_by_class_name("icon-edit").click()
        sleep(2)
        driver.find_element_by_xpath( "//li[contains(@class,'icon-edit')]//span[.='Edit This Instance']").click()



def library_menu(self, title, action):
    driver = self.driver
    item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='library_title' and text()='%s']" % title )))
    ActionChains(driver).click(item).perform()
    driver.find_element_by_class_name('%s' % action).click()

def library_content(self, title):
    driver = self.driver
    find = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='library_title' and text()='%s']" % title)))
    parent = find.find_element_by_xpath('..')
    return parent.text


def check_users_info(self):
    driver = self.driver
    username = driver.find_element_by_id("cu_login")
    username_value = username.get_attribute("value")
    first_name = driver.find_element_by_id("cu_first_name")
    first_name_value = first_name.get_attribute("value")
    last_name = driver.find_element_by_id("cu_last_name")
    last_name_value = last_name.get_attribute("value")
    email = driver.find_element_by_id("cu_email")
    email_value = email.get_attribute("value")
    language = driver.find_element_by_xpath("//option[@selected='selected']")
    timezone = driver.find_element_by_xpath("//option[@selected='selected']")
    return username_value, first_name_value, last_name_value, email_value, language.text, timezone.text


def edit_meta_title(self, filename, stamp, creator, album):
    driver = self.driver
    library_menu(self, filename, "icon-edit")
    sleep(2)
    driver.find_element_by_name("track_title").clear()
    driver.find_element_by_name("track_title").send_keys(stamp)
    driver.find_element_by_name("artist_name").clear()
    driver.find_element_by_name("artist_name").send_keys(creator)
    driver.find_element_by_name("album_title").clear()
    driver.find_element_by_name("album_title").send_keys(album)
    driver.find_element_by_id("editmdsave").click()

def edit_show(self, show_end):
    #this function is to edit show length for now
    driver = self.driver
    sleep(5)
    driver.find_element_by_xpath("//div[@id='schedule-add-show']/h3[2]").click()

    sleep(5)
    driver.find_element_by_id("add_show_end_time").clear()
    driver.find_element_by_id("add_show_end_time").send_keys(show_end)
    sleep(5)
    driver.find_element_by_class_name("ui-button-text").click()

    driver.refresh()










