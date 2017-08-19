from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import unittest
import pytest

class OrderTests(unittest.TestCase):


#Using login and browser set up in class setup
    def setUp(cls):
        FFprofile = webdriver.FirefoxProfile()
        FFprofile.set_preference('network.security.ports.banned.override', '6666')
        FFprofile.set_preference("browser.privatebrowsing.autostart", 'True')
        driver = webdriver.Firefox(FFprofile)
        username = "mari"
        password = "mari"
        lp=LoginPage(driver)
        lp.login(username, password)
        print("I am setup")
    #def test_createorder(cls):
        op=OrderPage(driver)
        op.getOrders
        op.addOrder()
        result=op.verifyAddOrderClicked()
        assert result == True
        op.addItemOrder(10)
        op.addItemOrder(1)
        op.acceptOrder()

        ordersExist=op.verifyOrdersExist()
        assert ordersExist==True

    def test_order2(cls):
        print("test2")


    def tearDown(cls):
        print ("I am teardown")
        webdriver.Firefox.quit()

#Cancel order

#verification for order status being accepted

#Dont accept order
        #op.acceptOrderCancel()
#verification for order being in status accepted

#Verification of user having orders.

