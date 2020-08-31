from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    """Класс для работы со странцией корзины"""

    def __init__(self, *args, **kwargs):
        """Метод для инициализации класса"""

        super(BasketPage, self).__init__(*args, *kwargs)

    def should_products_in_basket_disappeare(self):
        """Метод для проверки отсутствия товаров в корзине"""

        assert self.is_disappeared(*BasketPageLocators.PRODUCTS_IN_BASKET), \
                                    "Product in basket message is presented, but should not be"

    def should_be_empty_basket_message(self):
        """Метод для проверки наличия сообщения о том, что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
                                        "Page has not got message of empty basket"
    