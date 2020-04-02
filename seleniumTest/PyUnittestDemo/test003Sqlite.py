from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import unittest
import os as system, time
import sqlite3

class Login(unittest.TestCase):
    def setUp(self):
        #get the current directory absolute path
        currentWorkingDirectory = system.getcwd()
        currentWorkingDirectory = currentWorkingDirectory.replace("PyUnittestDemo","")
        #path to the chromeDriver
        chromeDriverAbsolutePath = currentWorkingDirectory + "drivers\chromedriver.exe"
        print(chromeDriverAbsolutePath)
        self.userDetailsCsvAbsolutePath = currentWorkingDirectory + "userdetail.csv"
        options =  Options()
        options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(executable_path=chromeDriverAbsolutePath,chrome_options=options)
        self.baseUrl = "http://newtours.demoaut.com/"
        self.sqliteConnect = sqlite3.connect('example.db')   
        
    def test_login(self):
        driver=self.browser
        driver.implicitly_wait(30)
        
        csvFile = open(self.userDetailsCsvAbsolutePath,"r")
        
        for line in csvFile:
            driver.get(self.baseUrl)
            te = line.rstrip("\n")
            record = te.split(",")            
            print(record)
            
            driver.find_element(By.NAME, "userName").send_keys(record[0])
            driver.find_element(By.XPATH, "//input[@name='password']").send_keys(record[1])
            driver.find_element(By.XPATH,"//input[@name='login' and @value='Login']").click()        
            
            # hard wait 
            time.sleep(3)
            headerElement = driver.find_element(By.XPATH,"//b[contains(text(),'Welcome back to') and contains(text(),'Mercury Tours!')]")
            print(headerElement.is_displayed())   
            self.assertTrue(headerElement.is_displayed(), "Login Success")
            
        csvFile.close
                       
    def tearDown(self):
        self.browser.quit()
        
        
if __name__ == "__main__":
    unittest.main()