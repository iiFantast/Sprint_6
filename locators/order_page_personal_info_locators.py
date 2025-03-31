from selenium.webdriver.common.by import By


class OrderPagePersonalAccLocators:
    name = [By.XPATH, './/input[@placeholder="* Имя"]']
    lastname = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_button = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    metro_stations = [(By.XPATH, './/div[text()="Черкизовская"]'),
                      (By.XPATH, './/div[text()="Бульвар Рокоссовского"]')]
    mobile_number = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, './/button[text()="Далее"]']