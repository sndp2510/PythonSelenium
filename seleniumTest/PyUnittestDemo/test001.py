from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import unittest
import os as system, time

class Login(unittest.TestCase):
    def setUp(self):
        #get the current directory absolute path
        currentWorkingDirectory = system.getcwd()
        currentWorkingDirectory = currentWorkingDirectory.replace("PyUnittestDemo","")
        #path to the chromeDriver
        chromeDriverAbsolutePath = currentWorkingDirectory + "drivers\chromedriver.exe"
        print(chromeDriverAbsolutePath)
        self.browser = webdriver.Chrome(executable_path=chromeDriverAbsolutePath)
        self.baseUrl = "http://newtours.demoaut.com/"       
        
    def test_login(self):
        driver=self.browser
        driver.implicitly_wait(30)
        driver.get(self.baseUrl)      
        driver.find_element(By.NAME, "userName").send_keys("mail@email.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("TestPassword")
        driver.find_element(By.XPATH,"//input[@name='login' and @value='Login']").click()
        # hard wait 
        #time.sleep(3)
        #headerElement = driver.find_element(By.XPATH,"//b[contains(text(),'Welcome back to') and contains(text(),'Mercury Tours!')]")
        #print(headerElement.is_displayed())   
        #self.assertTrue(headerElement.is_displayed(), "Login Success")
        
        #Explicit wait
        xpathHeaderElement = By.XPATH,"//b[contains(text(),'Welcome back to') and contains(text(),'Mercury Tours!')]"
        WebDriverWait(driver,20).until(expected_conditions.presence_of_element_located(xpathHeaderElement)) 
        
                        
    def tearDown(self):
        self.browser.quit()
        
        
if __name__ == "__main__":
    unittest.main()