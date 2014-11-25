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
        # change_time_zone(cls)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        # delete_all_tracks_from_db()
        # delete_all_users_from_db()
        driver.find_element_by_link_text("Logout").click()

        cls.driver.quit()

    @unittest.skip("skip this one")
    def test_currentUserPresent(self):
        driver = self.driver
        current_user = driver.find_element_by_class_name("name")
        self.assertEqual(current_user.text, tr_word('test'))

    @unittest.skip("skip this one")
    def test_admin_values(self):
        driver = self.driver
        driver.find_element_by_class_name("name").click()
        username = driver.find_element_by_id("cu_login")
        username_value = username.get_attribute("value")
        self.assertEqual(username_value, ADMIN_LOGIN)

    @unittest.skip("skip this one")
    def test_add_media_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("ADD MEDIA")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Add files to the upload queue and click the start button.") in source)
        self.assertTrue(tr_word("Drag files here.") in source)

    @unittest.skip("skip this one")
    def test_library_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("LIBRARY")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Advanced Search Options") in source)
        # self.assertTrue(tr_word("Open Media Builder") in source)
        self.assertTrue(tr_word("Show / hide columns") in source)

    @unittest.skip("skip this one")
    def test_calendar_present(self):
        driver = self.driver
        dates = month_name_year()
        driver.find_element_by_link_text(tr_word("CALENDAR")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("%s" % dates) in source)
        self.assertTrue(
            driver.find_element_by_xpath("//span[@class='fc-button-content' and text()='%s']" % tr_word("month")))
        self.assertTrue(
            driver.find_element_by_xpath("//span[@class='fc-button-content' and text()='%s']" % tr_word("week")))
        self.assertTrue(
            driver.find_element_by_xpath("//span[@class='fc-button-content' and text()='%s']" % tr_word("day")))

    @unittest.skip("skip this one")
    def test_dropsystem_present(self):
        driver = self.driver
        m1 = driver.find_element_by_link_text(tr_word("SYSTEM"))
        self.assertEqual(m1.text, tr_word('SYSTEM'))

    @unittest.skip("skip this one")
    def test_drophelp_present(self):
        driver = self.driver
        m1 = driver.find_element_by_link_text(tr_word("HISTORY"))
        self.assertEqual(m1.text, tr_word('HISTORY'))

    @unittest.skip("skip this one")
    def test_playerNowPresent(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("NOW PLAYING")).click()
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Show / hide columns") in source)

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
        driver.implicitly_wait(2)

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
        self.assertTrue(find_word(library_content.text, MP3_NAME), "MP3 name not present in Library")
        delete_track_from_db(uploadid)
        driver.implicitly_wait(2)

    @unittest.skip("skip this one")
    def test_create_Admin_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_admin(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_NAME)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Admin")))
        one = driver.find_element_by_xpath(
            "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(TADMIN_LOGIN))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = driver.find_element_by_id("users_datatable")
        self.assertFalse(find_word(after_deletion.text, tr_word(TADMIN_LOGIN)))
        driver.implicitly_wait(2)

    @unittest.skip("skip this one")
    def test_create_DJ_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_dj(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(DJ_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(DJ_NAME)))
        self.assertTrue(find_word(users.text, tr_word(DJ_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("DJ")))
        one = driver.find_element_by_xpath(
            "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(DJ_LOGIN))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = driver.find_element_by_id("users_datatable")
        self.assertFalse(find_word(after_deletion.text, tr_word(DJ_LOGIN)))
        driver.implicitly_wait(2)

    @unittest.skip("skip this one")
    def test_create_Guest_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_guest(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(GUEST_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_NAME)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Guest")))
        one = driver.find_element_by_xpath(
            "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(GUEST_LOGIN))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = driver.find_element_by_id("users_datatable")
        self.assertFalse(find_word(after_deletion.text, tr_word(GUEST_LOGIN)))
        driver.implicitly_wait(2)

    @unittest.skip("skip this one")
    def test_create_PR_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_pr(self)
        users = driver.find_element_by_id("users_datatable")
        self.assertTrue(find_word(users.text, tr_word(PR_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(PR_NAME)))
        self.assertTrue(find_word(users.text, tr_word(PR_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Program Manager")))
        one = driver.find_element_by_xpath(
            "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(PR_LOGIN))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = driver.find_element_by_id("users_datatable")
        self.assertFalse(find_word(after_deletion.text, tr_word(PR_LOGIN)))
        driver.implicitly_wait(2)


    #@unittest.skip("skip this one")
    def test_add_content_to_hour_show_delete_show(self):
        driver = self.driver
        stamp = time_stamper()
        stamped_show_name = stamp + SHOW_NAME
        #stamped_mp3_name = stamp + MP3_NAMEW
        go_to_folder(self, tr_word("ADD MEDIA"))
        #uploadid = upload_file(self, UPLOAD_MP3, MP3_NAME)
        ########upload_file(self, UPLOAD_MP3, MP3_NAME)
        date_now, day_number = my_date_time()
        # driver.find_element_by_xpath("//div[@class='fc-day-number' and text()='%s']" % day_number).click()
        # show_date_start = date
        #show_date_end = date
        #start_time = hour
        #end_time = hour
        create_show(self, stamped_show_name)
        time.sleep(2)
        #show_id = get_show_id(SHOW_NAME, date_now)
        #print show_id
        #add_content_to_show(self, show_id, uploadid)

        add_content_to_show_with_name(self,stamped_show_name, MP3_NAMEW)
        driver.implicitly_wait(3)
        self.assertTrue(driver.find_element_by_xpath("//div[@class='fc-day-number' and text()='%s']" % day_number))
        show_menu(self, stamped_show_name, "icon-overview")
        content = driver.find_element_by_class_name("datatable")
        print content.text
        driver.implicitly_wait(2)
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word(AD_NAME_60) in source)
        self.assertTrue(find_word(content.text, AD_CREATOR_60))
        #self.assertTrue(find_word(content.text, AD_NAME_60))
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        show_menu(self, stamped_show_name, "icon-delete")




if __name__ == '__main__':
    unittest.main()