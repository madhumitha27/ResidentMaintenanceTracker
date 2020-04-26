import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class staffTest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "staff1"
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
       AssignUnitButton = driver.find_element_by_xpath ( "/html/body/div/div[1]/nav/div[1]/div/a[1]" ).click ( )
       time.sleep ( 1 )
       assignButton = driver.find_element_by_xpath ("/html/body/div/div[2]/main/div/table/tbody/tr[1]/td[4]/a" ).click ( )
       time.sleep ( 1 )
       unitIdText = Select ( driver.find_element_by_id ( 'id_unitID' ) )
       unitIdText.select_by_visible_text ( '31' )
       time.sleep ( 1 )
       typeSelect = Select ( driver.find_element_by_id ( 'id_is_Primary' ) )
       typeSelect.select_by_value ( 'yes' )
       time.sleep ( 1 )
       updateButton = driver.find_element_by_xpath ( "/html/body/div/div[2]/main/div/div/form/button" ).click ( )
       time.sleep ( 1 )
       viewUnitButton = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/a" ).click ( )
       time.sleep ( 1 )
       reqLink = driver.find_element_by_xpath (
           "/html/body/div/div[1]/nav/div[1]/div/a[2]" ).click ( )
       time.sleep ( 1 )
       editLink = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/table/tbody/tr[1]/td[8]/a" ).click ( )
       statusSelect = Select ( driver.find_element_by_id ( 'id_status' ) )
       statusSelect.select_by_visible_text ( 'COMPLETED' )
       time.sleep ( 1 )
       statusUpdateButton = driver.find_element_by_xpath (
                   "/html/body/div/div[2]/main/div/div/form/button" ).click ( )
       time.sleep ( 1 )
       mailLink = driver.find_element_by_xpath (
           "/html/body/div/div[1]/nav/div[1]/div/a[3]" ).click ( )
       time.sleep ( 1 )
       subjectLink = driver.find_element_by_id ( "mail_id" )
       subjectLink.send_keys ( "mvasudevan@unomaha.edu" )
       time.sleep ( 1 )
       subjectLink = driver.find_element_by_id ( "id_subject" )
       subjectLink.send_keys ( "Hello All" )
       time.sleep ( 1 )
       contentLink = driver.find_element_by_id ( "id_content" )
       contentLink.send_keys ( "Just Test content" )
       time.sleep ( 1 )
       sendMailButton = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/div/form/button" ).click ( )
       time.sleep ( 1 )
       clickOption = driver.find_element_by_xpath (
           "/html/body/nav/div[2]/ul/li/a" ).click ( )
       time.sleep ( 1 )
       logout = driver.find_element_by_xpath (
           " / html / body / nav / div[2] / ul / li / div / a[2]" ).click ( )







   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
