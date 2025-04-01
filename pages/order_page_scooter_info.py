import allure

from locators.scooter_page_locators import ScooterLocators
from pages.base_page import BasePage


class ScooterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ScooterLocators()

    @allure.step('Выбрать дату')
    def set_date(self, date):
        self.click_on_element(self.locators.date_field)
        self.click_on_element(self.locators.date_in_calendar)

    @allure.step('Кликнуть на поле "Срок аренды"')
    def click_on_rental_period_button(self):
        self.click_on_element(self.locators.rental_period)

    @allure.step('Выбрать период')
    def click_on_period(self, period):
        self.click_on_element(self.locators.period_values[period])

    @allure.step('Выбрать цвет самоката')
    def set_scooter_color(self, color):
        self.click_on_element(self.locators.scooter_color[color])

    @allure.step('Заполнить поле "Комментарий"')
    def set_comment(self, comment):
        self.fill_input(self.locators.comment, comment)

    @allure.step('Выбрать период заказа самоката')
    def set_period(self, period):
        self.click_on_rental_period_button()
        self.click_on_period(period)

    @allure.step('Нажать кнопку "Заказать"')
    def click_on_order_button(self):
        self.click_on_element(self.locators.order_button)

    @allure.step('Нажать кнопку подтверждения заказа')
    def click_on_accept_order_button(self):
        self.click_on_element(self.locators.accept_order_button)

    @allure.step('Проверить, что отобразилось модальное окно об успешно созданном заказе')
    def check_modal_page_header(self):
        return self.element_is_displayed(self.locators.modal_page_header)

    @allure.step('Нажать кнопку "Посмотреть заказ"')
    def click_on_check_status_button(self):
        self.click_on_element(self.locators.check_status_button)

    @allure.step('Заполнить информацию о заказе самоката')
    def set_scooter_info(self, date, period, color, comment):
        self.set_date(date)
        self.set_period(period)
        self.set_scooter_color(color)
        self.set_comment(comment)
        self.click_on_order_button()
