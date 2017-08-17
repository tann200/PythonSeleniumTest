import requests
from base.selenium_driver import SeleniumDriver
from pages.login_page import LoginPage
from selenium.webdriver.support import select

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class OrderPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




# Define a function for adding an order
    def addOrder(self):
        add=self.getElement("Add order","link")
        add.click()

    def verifyAddOrderClicked(self):
        result = self.isElementPresent("orderDetails!addItem_order!acceptOrder", locatorType="ID")
        return result

    def chooseSupplier(self):
        #Needs a better way to find the supplier. Supplier list must be fetched to check supplier availability.
        supplierSelect = self.getElement("#orderDetails\!addItem_supplier > option:nth-child(3)","css")
        supplierSelect.click()

    def chooseProduct(self):
        # Needs a better way to find the product. Product list must be fetched to check product availability
        productSelect = self.getElement("#orderDetails\!addItem_product > option:nth-child(2)", "css")
        productSelect.click()

    def amountAdd(self,amountValue):
        amountAdd = self.getElement("orderDetails!addItem_amount", "ID")
        amountAdd.send_keys(amountValue)

    def clickAddButton(self):
        addButton=self.getElement("orderDetails!addItem_0","ID")
        #addButton = driver.find_element_by_css_selector('#orderDetails\!addItem_0')
        addButton.click()

    def acceptOrder(self):
        acceptButton=self.getElement("#orderDetails\!addItem_order\!acceptOrder", "css")
        acceptButton.click()
        self.alertAccept()

    def acceptOrderCancel(self):
        acceptButton = self.getElement("#orderDetails\!addItem_order\!acceptOrder", "css")
        acceptButton.click()
        self.alertDismiss()
# Adding items to order and order creation could be implemented using POST methods. Needs further investigation.
    def addItemOrder(self, amountValue):
        self.chooseSupplier()
        self.chooseProduct()
        self.amountAdd(amountValue)
        self.clickAddButton()

    def cancelOrder(self):
        cancelButton = self.getElement("#orderDetails\!addItem_order\!cancelOrder", "css")
        cancelButton.click()
        self.alertAccept()

    def cancelOrderCancel(self):
        cancelButton = self.getElement("#orderDetails\!addItem_order\!cancelOrder", "css")
        cancelButton.click()
        self.alertDismiss()









#Define a function for adding items to an order

#Define a function for placing the order

#Define a function for checking whether the user has any orders

#Define a function for changing an existing order

#Define a function for removing an existing order