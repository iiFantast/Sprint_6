import time

import allure
import pytest
from pages.base_page import BasePage
from pages.order_page_personal_info import OrderPage
from pages.order_page_scooter_info import ScooterPage


class TestOrder:
    # name = ['Василий', 'Георгий']
    # lastname = ['Иванов', 'Петров']

    @allure.title('Тест кейс оформления заказа самоката')
    @pytest.mark.parametrize('name, lastname, order_button, color, period, station', [('Василий', 'Иванов', 0, 0, 0, 0)
        , ('Георгий', 'Петров', 1, 1, 1, 1)])
    def test_make_order(self, driver, name, lastname, order_button, period, color, station):
        base_page = BasePage(driver)
        base_page.get_on_base_url()
        base_page.accept_cookie()
        base_page.click_on_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.set_personal_information(name, lastname, 'Какая-то Улица', '88005553535', station)
        scooter_page = ScooterPage(driver)
        scooter_page.set_scooter_info('08.03.2025', 0, color, 'тестовый комментарий')
        scooter_page.click_on_accept_order_button()
        assert scooter_page.check_modal_page_header()
        scooter_page.click_on_check_status_button()
        assert base_page.check_redirect_to_base_page_click_on_scooter() == base_page.base_url
        assert base_page.check_redirect_to_dzen_click_on_yandex_logo() == base_page.dzen_url
