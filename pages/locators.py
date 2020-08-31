from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket-items")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_REG_INPUT = (By.CSS_SELECTOR, ".register_form .form-group #id_registration-email")
    PASSWD_REG = (By.CSS_SELECTOR, ".register_form .form-group #id_registration-password1")
    PASSWD_REG_CONF = (By.CSS_SELECTOR, ".register_form .form-group #id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-primary")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")