from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default")

class BasketPageLocators():
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket-items")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")