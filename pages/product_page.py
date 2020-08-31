from base_page import BasePage

from locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_button()

    
    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_product_button.click()

    def should_be_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Adding button is not presented"

    def should_be_product_url(self):
        assert self.browser.current_url.index("catalogue"), "URL is incorrect"

    def should_be_correct_alert(self):
        alert_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert alert_text == product_name, "Alert is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT), "Success message is presented, but should not be"

    def should_success_message_disappeare(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
