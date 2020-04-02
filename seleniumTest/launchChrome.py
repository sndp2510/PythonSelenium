import os
from selenium import webdriver

#get the current directory absolute path
currentWorkingDirectory = os.getcwd()
#path to the chromeDriver
chromeDriverAbsolutePath = currentWorkingDirectory + "\drivers\chromedriver.exe"
print(chromeDriverAbsolutePath)

# Launch chrome browser
browser = webdriver.Chrome(executable_path=chromeDriverAbsolutePath)
# set the implicit default wait time 
browser.implicitly_wait(30)
browser.get('https://www.selenium.dev/')

# Find the download tab
downloadButton = browser.find_element_by_xpath("//a[text()='Downloads']")

# Click on the download tab
downloadButton.click()

print(browser.title)
print(browser.current_window_handle)
print(browser.window_handles)

#Fetch all the links on the web page prints the link text and href
allLinks = browser.find_elements_by_tag_name("a")
for link in allLinks:
    print(link.text, " >> ",link.get_attribute("href"))

#Quit the browser
browser.quit()
