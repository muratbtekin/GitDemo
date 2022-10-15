from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    keys = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    check = (By.XPATH, "//*[@class='checkbox checkbox-primary']")
    submitText = (By.XPATH, "//*[@type='submit']")

    def sendKeys(self):
        return self.driver.find_element(*ConfirmPage.keys)
    #self.driver.find_element(By.ID, "country").send_keys("ind")

    def choose(self):
        return self.driver.find_element(*ConfirmPage.india)
    #self.driver.find_element(By.LINK_TEXT, "India").click()

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.check)
    #self.driver.find_element(By.XPATH, "//*[@class='checkbox checkbox-primary']").click()

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitText)

    #self.driver.find_element(By.XPATH, "//*[@type='submit']").click()