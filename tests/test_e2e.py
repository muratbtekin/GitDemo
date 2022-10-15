from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        #bi üstteki aslında bu: self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        #checkoutPage.clickButton().click()

        checkOutPage.clickButton().click()
        confirmPage = checkOutPage.checkOutItems()
        log.info("entering country name as 'ind'")
        confirmPage.sendKeys().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.choose().click()
        confirmPage.checkBox().click()
        confirmPage.submit().click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        log.info("The text received from application is " + successText)
        assert "Success! Thank you" in successText

