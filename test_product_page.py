from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage

import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
main_page_link = "http://selenium1py.pythonanywhere.com/"
@pytest.mark.parametrize('link', [link])
def test_add_product_to_basket(browser, link):
    test_link =  link
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_alert()    
    #time.sleep(5)

@pytest.mark.parametrize('link', [pytest.param(link, marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    test_link =  link
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [link])
def test_guest_cant_see_success_message(browser, link):
    test_link =  link
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message

@pytest.mark.parametrize('link', [pytest.param(link, marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    test_link =  link
    page = ProductPage(browser, test_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_success_message_disappeare()

@pytest.mark.parametrize('link', [link])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', [link])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.parametrize('link', [main_page_link])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)




@pytest.mark.parametrize('link', [link])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):