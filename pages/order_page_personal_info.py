import allure

from locators.order_page_personal_info_locators import OrderPagePersonalAccLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPagePersonalAccLocators()

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.fill_input(self.locators.name, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_lastname(self, lastname):
        self.fill_input(self.locators.lastname, lastname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.fill_input(self.locators.address, address)

    @allure.step('Кликнуть на поле "Станция метро"')
    def click_on_metro_station_button(self):
        self.click_on_element(self.locators.metro_station_button)

    @allure.step('Выбрать станцию метро из списка')
    def click_on_metro_station(self, station):
        self.click_on_element(self.locators.metro_stations[station])

    @allure.step('Заполнить поле "Телефон"')
    def set_number(self, mobile_number):
        self.fill_input(self.locators.mobile_number, mobile_number)

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(self.locators.next_button)

    @allure.step('Указать персональную информацию')
    def set_personal_information(self, name, lastname, address, mobile_number, station):
        self.set_name(name)
        self.set_lastname(lastname)
        self.set_address(address)
        self.click_on_metro_station_button()
        self.click_on_metro_station(station)
        self.set_number(mobile_number)
        self.click_next_button()
