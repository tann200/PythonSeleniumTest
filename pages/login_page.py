import requests
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#Defining the login, which can be later used by other tests

    def login(self,username, password):
        baseURL = "localhost:6666/webshop/"
        loginURL=("http://" + username + ":" + password + "@" + baseURL)
        self.driver.get(loginURL)
        print("Opening url " + baseURL + "using " + " username: " + username + " and password: "+ password)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
#Defining a function for successful login
    def verifyLoginSuccessful(self):
        result=self.isElementPresent("Add order",locatorType="link")
        return result


    def invalidLogin(self, username, password):
        self.driver.get("http://" + username + ":" + password + "@" + baseURL)
        print("Opening url " + baseURL + "using " + "username: " + username + "and password: " + password)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        #Here an assertion which checks HTTP 403 status
    def check403PageStatus(self,username, password):
        baseURL = "localhost:6666/webshop/"
        requestStatus = requests.get("http://" + username + ":" + password + "@" + baseURL)
        requestCode = requestStatus.status_code
        print("HTTP error: " + str(requestCode))
        if requestCode==403:
            return True
        else:
            return False
#Checking that the page is not accessible without username and password
    def check401PageStatus(self):
        baseURL = "localhost:6666/webshop/"
        requestStatus = requests.get("http://" + baseURL)
        requestCode = requestStatus.status_code
        print("HTTP error: " + str(requestCode))
        if requestCode == 401:
            return True
        else:
            return False










