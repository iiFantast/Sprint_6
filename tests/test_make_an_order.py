import time

import allure
import pytest
from pages.main_page import BasePage, MainPage
from pages.order_page_personal_info import OrderPage
from pages.order_page_scooter_info import ScooterPage
from urls import BASE_URL, DZEN_URL


class TestOrder:

    @allure.title('Тест кейс оформления заказа самоката')
    @pytest.mark.parametrize('name, lastname, order_button, color, period, station', [('Василий', 'Иванов', 0, 0, 0, 0)
        , ('Георгий', 'Петров', 1, 1, 1, 1)])
    def test_make_order(self, driver, name, lastname, order_button, period, color, station):
        main_page = MainPage(driver)
        main_page.get_on_base_url()
        main_page.accept_cookie()
        main_page.click_on_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.set_personal_information(name, lastname, 'Какая-то Улица', '88005553535', station)
        scooter_page = ScooterPage(driver)
        scooter_page.set_scooter_info('08.03.2025', 0, color, 'тестовый комментарий')
        scooter_page.click_on_accept_order_button()
        assert scooter_page.check_modal_page_header()
        scooter_page.click_on_check_status_button()
        assert main_page.check_redirect_to_main_page_click_on_scooter() == BASE_URL
        assert main_page.check_redirect_to_dzen_click_on_yandex_logo() == DZEN_URL
