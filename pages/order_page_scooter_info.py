import allure
from selenium.webdriver.common.by import By


class ScooterPage:
    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    date_in_calendar = [By.XPATH, './/div[@aria-label="Choose суббота, 8-е марта 2025 г."]']
    rental_period = [By.CLASS_NAME, 'Dropdown-control']
    period_values = [(By.XPATH, './/div[text()="двое суток"]'),
                     (By.XPATH, './/div[text()="сутки"]')
                     ]
    scooter_color = [(By.XPATH, './/input[@id="black"]'),
                     (By.XPATH, './/input[@id="grey"]')
                     ]
    comment = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    order_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    accept_order_button = [By.XPATH, './/button[text()="Да"]']
    modal_page_header = [By.XPATH, './/div[@class="Order_Modal__YZ-d3"]']
    check_status_button = [By.XPATH, './/button[text()="Посмотреть статус"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбрать дату')
    def set_date(self, date):
        self.driver.find_element(*self.date_field).click()
        self.driver.find_element(*self.date_in_calendar).click()

    @allure.step('Кликнуть на поле "Срок аренды"')
    def click_on_rental_period_button(self):
        self.driver.find_element(*self.rental_period).click()

    @allure.step('Выбрать период')
    def click_on_period(self, period):
        self.driver.find_element(*self.period_values[period]).click()

    @allure.step('Выбрать цвет самоката')
    def set_scooter_color(self, color):
        self.driver.find_element(*self.scooter_color[color]).click()

    @allure.step('Заполнить поле "Комментарий"')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step('Выбрать период заказа самоката')
    def set_period(self, period):
        self.click_on_rental_period_button()
        self.click_on_period(period)

    @allure.step('Нажать кнопку "Заказать"')
    def click_on_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Нажать кнопку подтверждения заказа')
    def click_on_accept_order_button(self):
        self.driver.find_element(*self.accept_order_button).click()

    @allure.step('Проверить, что отобразилось модальное окно об успешно созданном заказе')
    def check_modal_page_header(self):
        return self.driver.find_element(*self.modal_page_header).is_displayed()

    @allure.step('Нажать кнопку "Посмотреть заказ"')
    def click_on_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()

    @allure.step('Заполнить информацию о заказе самоката')
    def set_scooter_info(self, date, period, color, comment):
        self.set_date(date)
        self.set_period(period)
        self.set_scooter_color(color)
        self.set_comment(comment)
        self.click_on_order_button()
