from .pages.product_page import ProductPage

import pytest
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
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

