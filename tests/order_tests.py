from selenium import webdriver
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import unittest
import pytest



class TestTests(unittest.TestCase):
#Define a fixture for setup
    def setUp(cls):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        #FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        cls.driver = webdriver.Firefox(FFprofile)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)
        cls.lp.login("mari", "mari")
        print("I am a class level setup")


    def test_createOrder(self):
        print("I am a test")
        self.op=OrderPage(self.driver)
        self.op.addOrder()
        result = self.op.verifyAddOrderClicked()
        assert result == True
        self.op.addItemOrder(10)
        self.op.acceptOrder()
        ordersExist = self.op.verifyOrdersExist()
        assert ordersExist == True

    def test_createOrderInvalidInputs(self):
        print("User will try to create an order without entering supplier, product and amount")


#Cancel order

#verification for order status being accepted

#Dont accept order
        #op.acceptOrderCancel()
#verification for order being in status accepted

#Verification of user having orders.




    def tearDown(cls):
        print ("I am teardown")




