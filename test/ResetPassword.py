import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class ResetPassword(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://madaad.pythonanywhere.com/")
       menuLink = driver.find_element_by_xpath ( "/html/body/a[1]" ).click ( )
       time.sleep(1)
       loginLink = driver.find_element_by_xpath ( "/html/body/nav/ul/li[2]/a" ).click ( )
       time.sleep ( 1 )
       forgotPwdLink = driver.find_element_by_xpath ( "/html/body/div[2]/div/main/div/div/div/div/div[3]/div/a" ).click ( )
       time.sleep ( 1 )
       username = driver.find_element_by_id("id_email")
       username.send_keys("mvasudevan@unomaha.edu")
       time.sleep ( 1 )
       sendEmailButton = driver.find_element_by_xpath (
           "/html/body/div[2]/div/main/div/div/div/div/div[2]/form/p[2]/input" ).click ( )
       time.sleep ( 1 )
       assert "Mail Sent for resetting password"

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
