import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class residentTest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "resident1"
       pwd = "Welcome@123"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://madaad.pythonanywhere.com/")
       menuLink = driver.find_element_by_xpath ( "/html/body/a[1]" ).click ( )
       time.sleep ( 1 )
       loginEle = driver.find_element_by_xpath ( "/html/body/nav/ul/li[2]/a" ).click ( )
       time.sleep ( 1 )
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       time.sleep ( 1 )
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       time.sleep ( 1 )
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep ( 1 )
       reuestViewButton = driver.find_element_by_xpath ( "/html/body/div/div[1]/nav/div[1]/div/a[1]" ).click ( )
       time.sleep ( 1 )
       newrequestButton = driver.find_element_by_xpath ("/html/body/div/div[2]/main/div/a" ).click ( )
       time.sleep ( 1 )
       prioritySelect = Select ( driver.find_element_by_id ( 'id_priority' ) )
       prioritySelect.select_by_visible_text ( 'URGENT' )
       time.sleep ( 1 )
       typeSelect = Select ( driver.find_element_by_id ( 'id_type' ) )
       typeSelect.select_by_visible_text ( 'Building Interior' )
       time.sleep ( 1 )
       accessIn = driver.find_element_by_id ( 'id_accessInstructions' )
       accessIn.send_keys ( "Please enter between 10 AM to 4 PM" )
       time.sleep ( 1 )
       desc =  driver.find_element_by_id ( 'id_desc' )
       desc.send_keys ( "Please change the lights in living room ")
       time.sleep ( 1 )
       perSelect = Select ( driver.find_element_by_id ( 'id_perToEnter' ) )
       perSelect.select_by_visible_text ( 'YES' )
       time.sleep ( 1 )
       saveButton = driver.find_element_by_xpath ( "/html/body/div/div[2]/main/div/div/form/button" ).click ( )
       profileLink = driver.find_element_by_xpath (
           "/html/body/div/div[1]/nav/div[1]/div/a[2]" ).click ( )
       time.sleep ( 1 )
       profileEditLink = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/table/tbody/tr[6]/td[4]/a" ).click ( )
       time.sleep ( 1 )
       phNumber = driver.find_element_by_id ( 'id_phone_number' )
       phNumber.clear ( )
       phNumber.send_keys ( "6155788438" )
       time.sleep ( 1 )
       vehNumber = driver.find_element_by_id ( 'id_vehNumber' )
       vehNumber.clear ( )
       vehNumber.send_keys ( "VYI-3451" )
       time.sleep ( 1 )
       emailText = driver.find_element_by_id ( 'id_email' )
       emailText.clear ( )
       emailText.send_keys ( "groyce@unomaha.edu" )
       time.sleep ( 1 )
       profileUpdateLink = driver.find_element_by_xpath (
                   "/html/body/div/div[2]/main/div/form/button" ).click ( )
       time.sleep ( 1 )
       clickOption = driver.find_element_by_xpath (
           "/html/body/nav/div[2]/ul/li/a" ).click ( )
       time.sleep ( 1 )

       changePasswordLink= driver.find_element_by_xpath (
           "/html/body/nav/div[2]/ul/li/div/a[1]" ).click ( )
       time.sleep ( 1 )
       oldPwd = driver.find_element_by_id ( "id_old_password" )
       oldPwd.send_keys ( "Welcome@123" )
       time.sleep ( 1 )
       newPwd1 = driver.find_element_by_id ( "id_new_password1" )
       newPwd1.send_keys ( "Windows@123" )
       time.sleep ( 1 )
       newPwd2 = driver.find_element_by_id ( "id_new_password2" )
       newPwd2.send_keys ( "Windows@123" )
       time.sleep ( 1 )
       changeButton = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/div/form/div/p/input" ).click ( )
       time.sleep ( 1 )
       clickOption = driver.find_element_by_xpath (
           "/html/body/nav/div[2]/ul/li/a" ).click ( )
       time.sleep ( 1 )
       logout = driver.find_element_by_xpath (
           " / html / body / nav / div[2] / ul / li / div / a[2]" ).click ( )

       # select by value






   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
