__author__ = 'nareg'

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, sys
from datetime import datetime, timedelta
from funtion_box import *
from action_box import *
from settings import *
from selenium import webdriver



class TestSuperAdminActions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.base_url = BASIC_URL
        cls.verificationErrors = []
        cls.accept_next_alert = True

        login(cls, ADMIN_LOGIN, ADMIN_PASS)
        #change_time_zone(cls)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        #delete_all_tracks_from_db()
        delete_all_users_from_db()
        driver.find_element_by_link_text("Logout").click()

        cls.driver.quit()

    def test_currentUserPresent(self):
        driver = self.driver
        current_user = driver.find_element_by_class_name("name")
        self.assertEqual(current_user.text, tr_word('admin'))

    @unittest.skip("skip this one")
    def test_admin_values(self):
        driver = self.driver
        driver.find_element_by_class_name("name").click()
        username = driver.find_element_by_id("cu_login")
        username_value = username.get_attribute("value")
        self.assertEqual(username_value, ADMIN_LOGIN)


    def test_add_media_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("ADD MEDIA")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Add files to the upload queue and click the start button.") in source)
        self.assertTrue(tr_word("Drag files here.") in source)

    def test_library_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("LIBRARY")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Advanced Search Options") in source)
        self.assertTrue(tr_word("Open Media Builder") in source)
        self.assertTrue(tr_word("Show / hide columns") in source)

    def test_calendar_present(self):
        driver = self.driver
        dates = month_name_year()
        driver.find_element_by_link_text(tr_word("CALENDAR")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("%s" % dates) in source)

    def test_dropsystem_present(self):
        driver = self.driver
        m1 = driver.find_element_by_link_text(tr_word("SYSTEM"))
        self.assertEqual(m1.text, tr_word('SYSTEM'))

    def test_drophelp_present(self):
        driver = self.driver
        m1 = driver.find_element_by_link_text(tr_word("HISTORY"))
        self.assertEqual(m1.text, tr_word('HISTORY'))

    def test_playerNowPresent(self):
        driver = self.driver
        m1 = driver.find_element_by_link_text(tr_word("NOW PLAYING"))
        self.assertEqual(m1.text, tr_word('NOW PLAYING'))


    @unittest.skip("skip this one")
    def test_addMP3_file(self):
        driver = self.driver
        driver.refresh()
        go_to_folder(self, tr_word("ADD MEDIA"))
        add_file(self, UPLOAD_MP3)
        time.sleep(5)
        filetoupload = driver.find_element_by_class_name("plupload_delete")
        self.assertTrue(find_word(filetoupload.text, MP3_NAMEW), "Name not in upload field")
        self.assertTrue(find_word(filetoupload.text, "0"), "Percentage not 0")
        driver.refresh()
        handle_alert(self)

    @unittest.skip("skip this one")
    def test_startMP3_upload(self):
        driver = self.driver
        driver.refresh()
        go_to_folder(self, tr_word("ADD MEDIA"))
        uploadid = upload_file(self, UPLOAD_MP3, MP3_NAME)
        upload_done = driver.find_element_by_class_name("plupload_done")
        time.sleep(5)
        self.assertTrue(find_word(upload_done.text, MP3_NAMEW), "MP3 name not present")
        self.assertTrue(find_word(upload_done.text, "100"), "Percentage not 100")
        go_to_folder(self, tr_word("LIBRARY"))
        library_content = driver.find_element_by_id(utilize_id(uploadid))
        self.assertTrue(find_word(library_content.text, MP3_NAME), "MP3 name not present")
        delete_track_from_db(uploadid)


    @unittest.skip("skip this one")
    def test_create_Admin(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_admin(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_NAME)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LASTNAME)))
        self.assertTrue(find_word(users.text, "Admin"))
    @unittest.skip("skip this one")
    def test_create_DJ(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_dj(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(DJ_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(DJ_NAME)))
        self.assertTrue(find_word(users.text, tr_word(DJ_LASTNAME)))
        self.assertTrue(find_word(users.text, "DJ"))
    @unittest.skip("skip this one")
    def test_create_Guest(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_guest(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(GUEST_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_NAME)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_LASTNAME)))
        self.assertTrue(find_word(users.text, "Guest"))
    @unittest.skip("skip this one")
    def test_create_PR(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_pr(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(PR_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(PR_NAME)))
        self.assertTrue(find_word(users.text, tr_word(PR_LASTNAME)))
        self.assertTrue(find_word(users.text, "Program Manager"))

    @unittest.skip("skip this one")
    def test_add_content_to_show(self):
        go_to_folder(self, tr_word("ADD MEDIA"))
        uploadid = upload_file(self, UPLOAD_MP3, MP3_NAME)
        #date, hour = my_date_time()
        #show_date_start = date
        #show_date_end = date
        #start_time = hour
        #end_time = hour
        create_show(self, SHOW_NAME)
        time.sleep(2)
        show_id = get_show_id(SHOW_NAME, "2014-10-31")
        print show_id
        add_content_to_show(self, show_id, uploadid)
        driver = self.driver
        driver.find_element_by_xpath("//tr[@si_id='%s']" % show_id)
        driver.find_element_by_xpath("//div[@class='fc-day-content' and text()='15']")






if __name__ == '__main__':
    unittest.main()