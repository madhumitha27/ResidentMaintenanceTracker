import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class signupFeature(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       menuLink = driver.find_element_by_xpath ( "/html/body/a[1]" ).click ( )
       time.sleep(1)
       signupLink = driver.find_element_by_xpath ( "/html/body/nav/ul/li[3]/a" ).click ( )
       username = driver.find_element_by_id("id_username")
       username.send_keys("testStaff")
       time.sleep ( 1 )
       Email = driver.find_element_by_id("id_email")
       Email.send_keys("mvasudevan@unomaha.edu")
       time.sleep ( 1 )
       first_name = driver.find_element_by_id ( "id_first_name" )
       first_name.send_keys ( "test First Name" )
       time.sleep ( 1 )
       last_name = driver.find_element_by_id ( "id_last_name" )
       last_name.send_keys ( "test Last Name" )
       time.sleep ( 1 )
       password1 = driver.find_element_by_id ( "id_password1" )
       password1.send_keys ( "test@123" )
       time.sleep ( 1 )
       password2 = driver.find_element_by_id ( "id_password2" )
       password2.send_keys ( "test@123" )
       time.sleep ( 1 )
       typeSelect = Select ( driver.find_element_by_id ( 'id_group' ) )
       typeSelect.select_by_value ( '2' )
       time.sleep(1)
       signUpButton = driver.find_element_by_xpath (
           "/html/body/div/div/main/div/div/div/div/div[2]/form/p/button" ).click ( )
       time.sleep(1)
       loginButton = driver.find_element_by_xpath (
           "/html/body/div/div/main/div/div/div/div/div[2]/p/a" ).click ( )
       user = "testStaff"
       pwd = "test@123"
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In As Staff"
       time.sleep ( 1 )
       clickOption = driver.find_element_by_xpath (
           "/html/body/nav/div[2]/ul/li/a" ).click ( )
       time.sleep ( 1 )
       logout = driver.find_element_by_xpath (
           " / html / body / nav / div[2] / ul / li / div / a[2]" ).click ()
       # select by value

  





   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
