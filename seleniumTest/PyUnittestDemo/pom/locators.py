from selenium.webdriver.common.by import By

class MainPage(object):
    FINDFLIGHT = (By.XPATH,"//img[@alt='Find a Flight']")
    
    
class LoginPage(object):
    USERNAME = (By.NAME,"userName")
    PASSWORD = (By.NAME,"password")
    SIGNIN = (By.NAME,"login")
    
class WelcomePage(object):
    WELCOMEHEADER = By.XPATH,"//b[contains(text(),'Welcome back to') and contains(text(),'Mercury Tours!')]"
