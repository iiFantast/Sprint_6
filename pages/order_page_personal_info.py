from selenium.webdriver.common.by import By
import allure


class OrderPage:
    name = [By.XPATH, './/input[@placeholder="* Имя"]']
    lastname = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_button = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    metro_stations = [(By.XPATH, './/div[text()="Черкизовская"]'),
                      (By.XPATH, './/div[text()="Бульвар Рокоссовского"]')]
    mobile_number = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, './/button[text()="Далее"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_lastname(self, lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    @allure.step('Кликнуть на поле "Станция метро"')
    def click_on_metro_station_button(self):
        self.driver.find_element(*self.metro_station_button).click()

    @allure.step('Выбрать станцию метро из списка')
    def click_on_metro_station(self, station):
        self.driver.find_element(*self.metro_stations[station]).click()

    @allure.step('Заполнить поле "Телефон"')
    def set_number(self, mobile_number):
        self.driver.find_element(*self.mobile_number).send_keys(mobile_number)

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Указать персональную информацию')
    def set_personal_information(self, name, lastname, address, mobile_number, station):
        self.set_name(name)
        self.set_lastname(lastname)
        self.set_address(address)
        self.click_on_metro_station_button()
        self.click_on_metro_station(station)
        self.set_number(mobile_number)
        self.click_next_button()
