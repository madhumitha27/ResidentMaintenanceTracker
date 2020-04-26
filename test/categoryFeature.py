import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class categoryFeature(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://madaad.pythonanywhere.com/admin/")
       time.sleep ( 1 )
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(1)
       categoryLink = driver.find_element_by_xpath ( "/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/th/a" ).click ( )
       time.sleep(1)
       addCategory = driver.find_element_by_xpath ("/html/body/div/div[3]/div/ul/li/a" ).click ( )
       time.sleep ( 1)
       unitID = driver.find_element_by_id ( 'id_catID' )
       unitID.send_keys ( "777" )
       time.sleep ( 1 )
       aptNo = driver.find_element_by_id ( 'id_type' )
       aptNo.send_keys ( "Building Interior" )
       time.sleep ( 1 )
       saveButton = driver.find_element_by_xpath ( " /html/body/div[1]/div[3]/div/form/div/div/input[1]" ).click ( )
       time.sleep ( 1 )
       logout = driver.find_element_by_xpath (
           "/html/body/div[1]/div[1]/div[2]/a[3]" ).click ( )

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
