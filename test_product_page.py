import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.parametrize('link', [LINK])
def test_add_product_to_basket(browser, link):
    test_link = link
    page = ProductPage(browser, test_link)
    page.open()
    #page.should_success_message_disappeare()
    page.should_not_be_success_message()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_alert()
    # time.sleep(5)


@pytest.mark.parametrize('link', [pytest.param(LINK, marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    test_link = link
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [LINK])
def test_guest_cant_see_success_message(browser, link):
    test_link = link
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [pytest.param(LINK, marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    test_link = link
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_success_message_disappeare()


@pytest.mark.parametrize('link', [LINK])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [LINK])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', [MAIN_PAGE_LINK])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_products_in_basket_disappeare()
    basket_page.should_be_empty_basket_message()


@pytest.mark.parametrize('link', [LINK])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_products_in_basket_disappeare()
    basket_page.should_be_empty_basket_message()
