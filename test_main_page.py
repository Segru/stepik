import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


class TestLoginFromMainPage():
    LINK = "http://selenium1py.pythonanywhere.com/"

    @pytest.mark.parametrize('link', [LINK])
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.parametrize('link', [LINK])
    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
