from selenium.webdriver.common.by import By

class ScooterLocators:
    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    date_in_calendar = [By.XPATH, './/div[@aria-label="Choose среда, 2-е апреля 2025 г."]']
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