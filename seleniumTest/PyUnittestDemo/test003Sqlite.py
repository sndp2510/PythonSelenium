from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import unittest
import os as system, time
import sqlite3
from sqlite3 import Error


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
        
        self.examleDbAbsolutePath = currentWorkingDirectory + "example.sqlite"        
        
        
        
    def test_login(self):
        driver=self.browser
        driver.implicitly_wait(30)
        
        
        print(self.examleDbAbsolutePath)
        create_connection = self.create_connection(self.examleDbAbsolutePath)
        rows = self.select_query(create_connection, "select username, password from userdetails")
        
        for row in rows:
            
            driver.get(self.baseUrl)
            print(">>", row)
            
            driver.find_element(By.NAME, "userName").send_keys(row[0])
            driver.find_element(By.XPATH, "//input[@name='password']").send_keys(row[1])
            driver.find_element(By.XPATH,"//input[@name='login' and @value='Login']").click()        
            
            # hard wait 
            time.sleep(3)
            headerElement = driver.find_element(By.XPATH,"//b[contains(text(),'Welcome back to') and contains(text(),'Mercury Tours!')]")
            print(headerElement.is_displayed())   
            self.assertTrue(headerElement.is_displayed(), "Login Success")
            
        
                       
    def tearDown(self):
        self.browser.quit()
        
    
    #Method to create a connection with sqlite database
    def create_connection(self,db_file):
                  
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
     
        return conn    
    
    
    #Accept the connection object and execute query and close connection
    def select_query (self, conn, queryStr):
        try:
            print(queryStr)
            cur=conn.cursor()
            cur.execute(queryStr)
            
            rows = cur.fetchall()
            return rows
        
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
            
        
if __name__ == "__main__":
    unittest.main()