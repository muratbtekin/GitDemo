from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    buttonClick = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    #driver.find_elements(By.CSS_SELECTOR, ".card-title a"
    #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
    def getCardTitles(self):

        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):

        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickButton(self):
        return self.driver.find_element(*CheckOutPage.buttonClick)
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

    def checkOutItems(self):

        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

