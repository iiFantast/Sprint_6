import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class TestQuestion:

    @allure.title('Тест кейс открытие текста при клике на первый вопрос')
    def test_first_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(0)
        assert base_page.get_answer_text(0) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Тест кейс открытие текста при клике на второй вопрос')
    def test_second_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(1)
        assert base_page.get_answer_text(1) == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься '
                                                'с друзьями, можете просто сделать несколько заказов — один за другим.')

    @allure.title('Тест кейс открытие текста при клике на третий вопрос')
    def test_third_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(2)
        assert base_page.get_answer_text(2) == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в '
                                                'течение дня. Отсчёт времени аренды начинается с момента, '
                                                'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
                                                '20:30, суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Тест кейс открытие текста при клике на четвертый вопрос')
    def test_fourth_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(3)
        assert base_page.get_answer_text(3) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Тест кейс открытие текста при клике на пятый вопрос')
    def test_fiveth_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(4)
        assert base_page.get_answer_text(4) == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в '
                                                'поддержку по красивому номеру 1010.')

    @allure.title('Тест кейс открытие текста при клике на шестой вопрос')
    def test_sixth_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(5)
        assert base_page.get_answer_text(5) == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь '
                                                'суток — даже если будете кататься без передышек и во сне. Зарядка не'
                                                ' понадобится.')

    @allure.title('Тест кейс открытие текста при клике на седьмой вопрос')
    def test_seventh_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(6)
        assert base_page.get_answer_text(6) == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки '
                                                'тоже не попросим. Все же свои.')

    @allure.title('Тест кейс открытие текста при клике на восьмой вопрос')
    def test_eighth_question(self, driver):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_question(7)
        assert base_page.get_answer_text(7) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
