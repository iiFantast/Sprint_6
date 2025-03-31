from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, DZEN_URL


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Нажимаем кнопку "Принять куки"')
    def accept_cookie(self):
        self.click_on_element(self.locators.cookie_button)


    @allure.step('Кликнуть на вопрос')
    def click_on_question(self, question):
        self.click_on_element(self.locators.questions[question])

    @allure.step('Перейти на главную страницу')
    def get_on_base_url(self):
        self.get_on_url(BASE_URL)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, arg):
        return self.get_text_of_element(self.locators.answers[arg])

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_element(self.locators.order_button[button])

    @allure.step('Кликнуть на лого самоката')
    def click_on_scooter_logo(self):
        self.click_on_element(self.locators.scooter_logo)

    @allure.step('Кликнуть на лого Яндекса')
    def click_on_yandex_logo(self):
        self.click_on_element(self.locators.yandex_logo)

    @allure.step('Проверить, что открылась главная при клике на лого самоката')
    def check_redirect_to_base_page_click_on_scooter(self):
        self.click_on_scooter_logo()
        current_url = self.driver.current_url
        return current_url

    @allure.step('Проверить, что открылась страница дзена при клике на лого Яндекса')
    def check_redirect_to_dzen_click_on_yandex_logo(self):
        current_window = self.driver.current_window_handle
        self.click_on_yandex_logo()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(DZEN_URL))
        current_url = self.driver.current_url
        return current_url
