from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_message(self, product_name):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Сообщение о добавлении товара в корзину не найдено"
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert message_name == product_name, \
            f"Название в сообщении '{message_name}' не совпадает с названием товара '{product_name}'"

    def should_be_basket_total_message(self, product_price):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
            "Сообщение со стоимостью корзины не найдено"
        basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert basket_total == product_price, \
            f"Стоимость корзины '{basket_total}' не совпадает с ценой товара '{product_price}'"