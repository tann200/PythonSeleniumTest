from selenium import webdriver
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import unittest
import pytest


class TestTests(unittest.TestCase):
    # Define a fixture for setup
    def setUp(cls):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        # FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        cls.driver = webdriver.Firefox(FFprofile)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        print("I am a class level setup")

    def test_1_validLogin(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("mari", "mari")
        print("I am test")
        result = self.lp.verifyLoginSuccessful()
        print(result)
        assert result == True

    # Test for invalid login scenario with wrong username and correct password.
    def test_invalidLoginUsername(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check403PageStatus("mari123", "mari")
        assert requestStatus == True

    def test_invalidLoginUsernameAndPassword(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check403PageStatus("maris", "maris")
        assert requestStatus == True

    def test_emptyLoginUsernameAndCorrectPassword(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check403PageStatus("", "maris")
        assert requestStatus == True

    def test_correctLoginUsernameAndEmptyPassword(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check403PageStatus("mari", "")
        assert requestStatus == True

    def test_EmptyLoginUsernameAndPassword(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check401PageStatus()
        assert requestStatus == True

    def test_invalidLoginPassword(self):
        self.lp = LoginPage(self.driver)
        requestStatus = self.lp.check403PageStatus("mari", "mari1")
        assert requestStatus == True

    def tearDown(cls):
        cls.driver.close()
        print("I am teardown")




