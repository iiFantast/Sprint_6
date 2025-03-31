from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL, DZEN_URL
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_of_element(self, locator):
       return self.driver.find_element(*locator).text

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def get_on_url(self, url):
        self.driver.get(url)

    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def element_is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

