from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import unittest
import pytest

class OrderTests(unittest.TestCase):


#This has to be converted to a setup method to ensure user is logged in before doing order related stuff
    def test_login_before_order(self):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        driver = webdriver.Firefox(FFprofile)
        lp = LoginPage(driver)
        self.lp=LoginPage(self)
        username = "mari"
        password = "mari"

        lp.login(username, password)
        # Following code should be in another method called
    #def test_createorder(self):
        op = OrderPage(driver)
        op.addOrder()
        result=op.verifyAddOrderClicked()
        assert result == True
        op.addItemOrder(10)
        op.addItemOrder(1)

#Start creating an order and add an item to order
     #def test_add_item_order(self):


#Accept order
        #op.acceptOrder()

#Cancel order

#verification for order status being accepted

#Dont accept order
        #op.acceptOrderCancel()
#verification for order being in status accepted

#Verification of user having orders.

