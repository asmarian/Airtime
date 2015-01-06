__author__ = 'nareg'

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, re, sys
from time import sleep
from datetime import timedelta
from datetime import datetime
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
        # change_time_zone(cls, TIME_ZONE)

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
        driver.find_element_by_class_name("name").click()
        username_value, first_name_value, last_name_value, email_value, language, timezone = check_users_info(self)
        self.assertEqual(username_value, ADMIN_LOGIN)
        # check for the rest of the info


    @unittest.skip("skip this one")
    def test_add_media_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("ADD MEDIA")).click()
        source = driver.page_source
        sleep(2)
        self.assertTrue(tr_word("Add files to the upload queue and click the start button.") in source)
        self.assertTrue(tr_word("Drag files here.") in source)

    @unittest.skip("skip this one")
    def test_library_present(self):
        driver = self.driver
        driver.find_element_by_link_text(tr_word("LIBRARY")).click()
        source = driver.page_source
        sleep(2)
        self.assertTrue(tr_word("Advanced Search Options") in source)
        # self.assertTrue(tr_word("Open Media Builder") in source)
        self.assertTrue(tr_word("Show / hide columns") in source)

    @unittest.skip("skip this one")
    def test_calendar_present(self):
        driver = self.driver
        dates = month_name_year()
        driver.find_element_by_link_text(tr_word("CALENDAR")).click()
        source = driver.page_source
        sleep(2)
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
        source = driver.page_source
        driver.implicitly_wait(2)
        self.assertTrue(tr_word("Show / hide columns") in source)

    @unittest.skip("skip this one")
    def test_addMP3_file(self):
        driver = self.driver
        driver.refresh()
        go_to_folder(self, tr_word("ADD MEDIA"))
        add_file(self, UPLOAD_MP3)
        driver.implicitly_wait(2)
        filetoupload = driver.find_element_by_class_name("plupload_delete")
        driver.implicitly_wait(2)
        self.assertTrue(find_word(filetoupload.text, MP3_NAMEW), "Name not in upload field")
        self.assertTrue(find_word(filetoupload.text, "0"), "Percentage not 0")
        driver.refresh()
        handle_alert(self)


    @unittest.skip("skip this one")
    def test_startMP3_upload_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        upload_done = driver.find_element_by_class_name("plupload_done")
        driver.implicitly_wait(2)
        self.assertTrue(find_word(upload_done.text, MP3_NAMEW), "MP3 name not present")
        self.assertTrue(find_word(upload_done.text, "100"), "Percentage not 100")
        go_to_folder(self, tr_word("LIBRARY"))
        library_menu(self, MP3_NAMEW, "icon-delete")
        handle_alert(self)
        # self.assertTrue(find_word(library_content.text, MP3_NAME), "MP3 name not present in Library")


    @unittest.skip("skip this one")
    def test_startMP3_upload_edit_title(self):
        driver = self.driver
        # driver.refresh()
        # find = library_content(self, MP3_NAMEW)
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        upload_done = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "plupload_done")))
        self.assertTrue(find_word(upload_done.text, MP3_NAMEW), "MP3 name not present")
        self.assertTrue(find_word(upload_done.text, "100"), "Percentage not 100")
        go_to_folder(self, tr_word("LIBRARY"))
        stamped_file_name = time_stamper() + MP3_NAMEW
        edit_meta_title(self, MP3_NAMEW, stamped_file_name, "tester", "test_music")
        lib_content = library_content(self, stamped_file_name)
        self.assertTrue(find_word(lib_content, stamped_file_name))


        # library_menu(self, stamped_file_name,"icon-delete")
        # handle_alert(self)
        #self.assertTrue(find_word(library_content.text, MP3_NAME), "MP3 name not present in Library")


    @unittest.skip("skip this one")
    def test_create_Admin_logout_login_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_admin(self)
        sleep(5)
        users = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_NAME)))
        self.assertTrue(find_word(users.text, tr_word(TADMIN_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Admin")))
        driver.find_element_by_link_text("Logout").click()
        login(self, TADMIN_LOGIN, TADMIN_PASS)
        driver.find_element_by_id("current-user").click()
        username_value, first_name_value, last_name_value, email_value, language, timezone = check_users_info(self)
        sleep(2)
        self.assertEqual(username_value, TADMIN_LOGIN)
        self.assertEqual(first_name_value, TADMIN_NAME)
        self.assertEqual(last_name_value, TADMIN_LASTNAME)
        self.assertEqual(email_value, TADMIN_EMAIL)

        go_to_subfolder(self, "SYSTEM", "Users")
        driver.find_element_by_link_text("Logout").click()
        login(self, ADMIN_LOGIN, ADMIN_PASS)
        go_to_subfolder(self, "SYSTEM", "Users")
        one = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                              ((By.XPATH,
                                                "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(
                                                    TADMIN_LOGIN))))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertFalse(find_word(after_deletion.text, tr_word(TADMIN_LOGIN)))


    @unittest.skip("skip this one")
    def test_create_DJ_delete(self):
        driver = self.driver
        go_to_subfolder(self, "SYSTEM", "Users")
        create_dj(self)
        driver.refresh()
        users = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertTrue(find_word(users.text, tr_word(DJ_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(DJ_NAME)))
        self.assertTrue(find_word(users.text, tr_word(DJ_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("DJ")))
        one = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH,
            "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(DJ_LOGIN))))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertFalse(find_word(after_deletion.text, tr_word(DJ_LOGIN)))


    @unittest.skip("skip this one")
    def test_create_Guest_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_guest(self)
        sleep(5)
        users = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertTrue(find_word(users.text, tr_word(GUEST_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_NAME)))
        self.assertTrue(find_word(users.text, tr_word(GUEST_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Guest")))
        one = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                              ((By.XPATH,
                                                "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(
                                                    GUEST_LOGIN))))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertFalse(find_word(after_deletion.text, tr_word(GUEST_LOGIN)))


    @unittest.skip("skip this one")
    def test_create_PR_delete(self):
        driver = self.driver
        driver.refresh()
        go_to_subfolder(self, "SYSTEM", "Users")
        create_pr(self)
        sleep(5)
        users = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertTrue(find_word(users.text, tr_word(PR_LOGIN)))
        self.assertTrue(find_word(users.text, tr_word(PR_NAME)))
        self.assertTrue(find_word(users.text, tr_word(PR_LASTNAME)))
        self.assertTrue(find_word(users.text, tr_word("Program Manager")))
        one = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                              ((By.XPATH,
                                                "//td[@class='' and text()='%s']/..//span[@class='ui-icon ui-icon-closethick']" % tr_word(
                                                    PR_LOGIN))))
        ActionChains(driver).click(one).perform()
        driver.refresh()
        after_deletion = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "users_datatable")))
        self.assertFalse(find_word(after_deletion.text, tr_word(PR_LOGIN)))


    @unittest.skip("skip this one")
    def test_add_content_to_hour_show_delete_show(self):
        driver = self.driver
        stamped_show_name = time_stamper() + SHOW_NAME
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        show_start, show_end = setup_time(HOUR_SHOW)
        create_show(self, stamped_show_name, show_start, show_end, "no_repeat", "no_link")
        go_to_folder(self, tr_word("LIBRARY"))
        stamped_file_name = time_stamper() + MP3_NAMEW
        edit_meta_title(self, MP3_NAMEW, stamped_file_name, "tester", "test_album")
        driver.refresh()
        go_to_folder(self, tr_word("CALENDAR"))
        add_content_to_show_with_name(self, stamped_show_name, stamped_file_name)
        sleep(5)
        show_menu(self, stamped_show_name, "icon-overview")
        content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datatable")))
        self.assertTrue(find_word(content.text, AD_CREATOR_60))
        self.assertTrue(find_word(content.text, AD_NAME_60))
        self.assertTrue(find_word(content.text, stamped_file_name))
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        sleep(2)
        show_menu(self, stamped_show_name, "icon-delete")

    @unittest.skip("skip this one")
    def test_add_content_to_hour_linked_show_delete_show(self):
        driver = self.driver
        stamped_show_name = time_stamper() + SHOW_NAME
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        show_start, show_end = setup_time(HOUR_SHOW)
        create_show(self, stamped_show_name, show_start, show_end, "repeat", "link")
        go_to_folder(self, tr_word("LIBRARY"))
        stamped_file_name = time_stamper() + MP3_NAMEW
        edit_meta_title(self, MP3_NAMEW, stamped_file_name, "tester", "test_album")
        driver.refresh()
        go_to_folder(self, tr_word("CALENDAR"))
        add_content_to_show_with_name(self, stamped_show_name, stamped_file_name)
        show_menu(self, stamped_show_name, "icon-overview")
        content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datatable")))
        self.assertTrue(find_word(content.text, AD_CREATOR_60))
        self.assertTrue(find_word(content.text, AD_NAME_60))
        self.assertTrue(find_word(content.text, stamped_file_name))
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        sleep(2)
        show_menu(self, stamped_show_name, "delete_instances")

    @unittest.skip("skip this one")
    def test_create_longer_show_test_correct_number_of_ads(self):
        driver = self.driver
        stamped_show_name = time_stamper() + SHOW_NAME
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        show_start, show_end = setup_time(SHOW_LENGTH)
        create_show(self, stamped_show_name, show_start, show_end, "no_repeat", "no_link")
        go_to_folder(self, tr_word("LIBRARY"))
        stamped_file_name = time_stamper() + MP3_NAMEW
        edit_meta_title(self, MP3_NAMEW, stamped_file_name, "tester", "test_album")
        driver.refresh()
        go_to_folder(self, tr_word("CALENDAR"))
        add_content_to_show_with_name(self, stamped_show_name, stamped_file_name)
        sleep(5)
        show_menu(self, stamped_show_name, "icon-overview")
        # check to see if the right number of ads were added to x length of show
        content = driver.find_elements_by_xpath("//td[text()='%s']" % AD_CREATOR_60)
        self.assertEqual(len(content), SHOW_LENGTH)
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        sleep(2)
        show_menu(self, stamped_show_name, "icon-delete")

    def test_create_linked_show_check_number_of_ads_in_instance(self):
        driver = self.driver
        stamped_show_name = time_stamper() + SHOW_NAME
        go_to_folder(self, tr_word("ADD MEDIA"))
        upload_file(self, UPLOAD_MP3, MP3_NAME)
        show_start, show_end = setup_time(HOUR_SHOW)
        create_show(self, stamped_show_name, show_start, show_end, "repeat", "link")
        go_to_folder(self, tr_word("LIBRARY"))
        stamped_file_name = time_stamper() + MP3_NAMEW
        edit_meta_title(self, MP3_NAMEW, stamped_file_name, "tester", "test_album")
        driver.refresh()
        go_to_folder(self, tr_word("CALENDAR"))
        add_content_to_show_with_name(self, stamped_show_name, stamped_file_name)
        driver.refresh()
        show_menu(self, stamped_show_name, "icon-overview")
        content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datatable")))
        self.assertTrue(find_word(content.text, AD_CREATOR_60))
        self.assertTrue(find_word(content.text, AD_NAME_60))
        self.assertTrue(find_word(content.text, stamped_file_name))
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        sleep(2)
        show_menu(self, stamped_show_name, "delete_instance")
        driver.refresh()
        show_menu(self, stamped_show_name, "icon-overview")
        content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datatable")))
        #check to see if the instance has the correct number of ads
        self.assertTrue(find_word(content.text, AD_CREATOR_60))
        self.assertTrue(find_word(content.text, AD_NAME_60))
        self.assertTrue(find_word(content.text, stamped_file_name))
        driver.find_element_by_xpath("//button[@class='btn' and text()='Ok']").click()
        show_menu(self, stamped_show_name, "edit_instance")
        new_show_end = add_time(SHOW_LENGTH)
        edit_show(self, new_show_end)
        show_menu(self, stamped_show_name, "icon-overview")
        # check to see if the right number of ads were added to x length of show
        content1 = driver.find_elements_by_xpath("//td[text()='%s']" % AD_CREATOR_60)
        self.assertEqual(SHOW_LENGTH, len(content1))
        show_menu(self, stamped_show_name, "delete_instances")


if __name__ == '__main__':
    unittest.main()