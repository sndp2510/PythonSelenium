import os
from selenium import webdriver

currentWorkingDirectory = os.getcwd()
geckoDriverAbsolutePath = currentWorkingDirectory + "\drivers\geckodriver.exe"
print(geckoDriverAbsolutePath)
browser = webdriver.Firefox(executable_path=geckoDriverAbsolutePath)
browser.get('https://www.selenium.dev/')
browser.quit()