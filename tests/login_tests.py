from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):


#Test for valid login scenario

    def test_validLogin(self):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        driver = webdriver.Firefox(FFprofile)
        lp = LoginPage(driver)
        username = "mari"
        password = "mari"
        print("set usernames")
        lp = LoginPage(self.driver)
        lp.login(username, password)

        result=lp.verifyLoginSuccessful()
        assert result==True
        yield



#Test for invalid login scenario with wrong password and correct user.
    @pytest.mark.run(order=1)
    def test_invalidLoginPassword(self):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        driver = webdriver.Firefox(FFprofile)
        username = "mari"
        password = "maris"
        lp = LoginPage(driver)
        requestStatus=lp.check403PageStatus(username,password)
        assert requestStatus == True
        driver.close()


"""

#Test for invalid login scenario with wrong username and correct password.
def test_invalidLoginUsername(self):
    FFprofile = webdriver.FirefoxProfile()
    FFprofile.set_preference('network.security.ports.banned.override', '6666')
    FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
    driver = webdriver.Firefox(FFprofile)
    username = "mari1"
    password = "mari"
    lp = LoginPage(driver)
    requestStatus=lp.check403PageStatus(username,password)
    assert requestStatus == True
    driver.close()
#Test for invalid login scenario with incorrect user and incorrect password.
def test_invalidLoginUsernameAndPassword(self):
    FFprofile = webdriver.FirefoxProfile()
    FFprofile.set_preference('network.security.ports.banned.override', '6666')
    FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
    driver = webdriver.Firefox(FFprofile)
    username = "mari1"
    password = "mari1"
    lp = LoginPage(driver)
    requestStatus=lp.check403PageStatus(username,password)
    assert requestStatus == True
    driver.close()
#Test for invalid login scenario with empty username and  valid password.
def test_emptyLoginUsername(self):
    FFprofile = webdriver.FirefoxProfile()
    FFprofile.set_preference('network.security.ports.banned.override', '6666')
    FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
    driver = webdriver.Firefox(FFprofile)
    username = ""
    password = "mari"
    lp = LoginPage(driver)
    requestStatus=lp.check403PageStatus(username,password)
    assert requestStatus == True
    driver.close()
#Test for invalid login scenario with valid username and empty login password.
def test_emptyLoginPassword(self):
    FFprofile = webdriver.FirefoxProfile()
    FFprofile.set_preference('network.security.ports.banned.override', '6666')
    FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
    driver = webdriver.Firefox(FFprofile)
    username = "mari"
    password = ""
    lp = LoginPage(driver)
    requestStatus=lp.check403PageStatus(username,password)
    assert requestStatus == True
    driver.close()

def test_EmptyLoginUsernameAndPassword(self):
    FFprofile = webdriver.FirefoxProfile()
    FFprofile.set_preference('network.security.ports.banned.override', '6666')
    FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
    driver = webdriver.Firefox(FFprofile)
    lp = LoginPage(driver)
    requestStatus=lp.check401PageStatus()
    assert requestStatus == True
    driver.close()
"""







