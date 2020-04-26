import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class admintest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "Welcome@123"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       menuLink = driver.find_element_by_xpath ( "/html/body/a[1]" ).click ( )
       time.sleep(1)
       loginEle = driver.find_element_by_xpath ( "/html/body/nav/ul/li[2]/a" ).click ( )
       time.sleep ( 1 )
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(1)
       viewUnitButton = driver.find_element_by_xpath ( "/html/body/div/div[1]/nav/div[1]/div/a[1]" ).click ( )
       time.sleep(1)
       addUnitButton = driver.find_element_by_xpath ("/html/body/div/div[2]/main/div/a" ).click ( )
       time.sleep ( 1)
       unitID = driver.find_element_by_id ( 'id_unitID' )
       unitID.send_keys ( "777" )
       time.sleep ( 1 )
       aptNo = driver.find_element_by_id ( 'id_aptNo' )
       aptNo.send_keys ( "22" )
       time.sleep ( 1 )
       street = driver.find_element_by_id ( 'id_street' )
       street.send_keys ( "Pacific Street" )
       time.sleep (1 )
       state =  driver.find_element_by_id ( 'id_state' )
       state.send_keys ( "NE ")
       time.sleep ( 1 )
       city =  driver.find_element_by_id  ( 'id_city' )
       city.send_keys ( 'Elkhorn' )
       time.sleep ( 1 )
       zipCode = driver.find_element_by_id ( 'id_zipcode' )
       zipCode.send_keys ( '68022' )
       time.sleep ( 1 )
       saveButton = driver.find_element_by_xpath ( " /html/body/div/div[2]/main/div/div/form/button" ).click ( )
       time.sleep ( 1 )
       reportButton = driver.find_element_by_xpath (
           "/html/body/div/div[1]/nav/div[1]/div/a[3]" ).click ( )
       time.sleep ( 1 )
       fromDate = driver.find_element_by_id ( 'id_from_date' )
       fromDate.clear ( )
       fromDate.send_keys ( "04/01/2020" )
       time.sleep ( 1 )
       toDate = driver.find_element_by_id ( 'id_to_date' )
       toDate.clear ( )
       toDate.send_keys ( "04/30/2020" )
       time.sleep ( 1 )
       downloadButton = driver.find_element_by_xpath (
                   "/html/body/div/div[2]/main/div/div/form/button" ).click ( )

       time.sleep ( 1 )
       manageUsers = driver.find_element_by_xpath (
           "/html/body/div/div[1]/nav/div[1]/div/a[2]" ).click ( )
       time.sleep ( 1)
       editUser = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/table/tbody/tr[6]/td[6]/a" ).click ( )
       time.sleep ( 1 )
       firstName = driver.find_element_by_id ( 'id_first_name' )
       firstName.clear ( )
       firstName.send_keys ( "Bill1" )
       time.sleep ( 1 )
       lastName = driver.find_element_by_id ( 'id_last_name' )
       lastName.send_keys ( "Davis11" )
       lastName.clear ( )
       time.sleep (1 )
       email = driver.find_element_by_id ( 'id_email' )
       email.send_keys ( "mvasudevan@unomaha.edu" )
       email.clear ( )
       time.sleep ( 1 )
       username = driver.find_element_by_id ( 'id_username' )
       username.clear ( )
       username.send_keys ( "Dummy " )
       time.sleep ( 1 )
       saveUser = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/div/form/button" ).click ( )
       time.sleep ( 1 )
       deleteUser = driver.find_element_by_xpath (
           "/html/body/div/div[2]/main/div/table/tbody/tr[6]/td[7]/a" ).click ( )
       time.sleep ( 1)
       obj = driver.switch_to.alert
       time.sleep ( 1 )
       obj.accept ( )
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
