import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    base_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'
    questions = [
        (By.XPATH, '//div[text()="Сколько это стоит? И как оплатить?"]'),
        (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]'),
        (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]'),
        (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]'),
        (By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]'),
        (By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]'),
        (By.XPATH, '//div[text()="Можно ли отменить заказ?"]'),
        (By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]')
    ]
    answers = [
        (By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]'),
        (By.XPATH, './/p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                   'можете просто сделать несколько заказов — один за другим."]'),
        (By.XPATH, './/p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                   'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                   'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]'),
        (By.XPATH, './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]'),
        (By.XPATH, './/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                   'красивому номеру 1010."]'),
        (By.XPATH, './/p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                   'будете кататься без передышек и во сне. Зарядка не понадобится."]'),
        (By.XPATH, './/p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не '
                   'попросим. Все же свои."]'),
        (By.XPATH, './/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]')
    ]
    cookie_button = [By.ID, 'rcc-confirm-button']
    order_button = [(By.CLASS_NAME, 'Button_Button__ra12g'),
                    (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
                    ]
    scooter_logo = [By.XPATH, './/img[@alt="Scooter"]']
    yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку "Принять куки"')
    def accept_cookie(self):
        self.driver.find_element(*self.cookie_button).click()

    @allure.step('Кликнуть на вопрос')
    def click_on_question(self, arg):
        self.driver.find_element(*self.questions[arg]).click()

    @allure.step('Перейти на главную страницу')
    def get_on_base_url(self):
        self.driver.get(self.base_url)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, arg):
        return self.driver.find_element(*self.answers[arg]).text

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_on_order_button(self, order_button):
        self.driver.find_element(*self.order_button[order_button]).click()

    @allure.step('Кликнуть на лого самоката')
    def click_on_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Кликнуть на лого Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

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

        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(self.dzen_url))
        current_url = self.driver.current_url
        return current_url
