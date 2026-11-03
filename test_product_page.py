import pytest
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

#BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
#links = [f"{BASE_LINK}{n}" for n in range(10)]


#@pytest.mark.parametrize("link", links)
#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()

#    product_name = page.get_product_name()
#    product_price = page.get_product_price()

#    page.add_product_to_basket()
#    page.solve_quiz_and_get_code()

#   page.should_be_product_added_message(product_name)
#   page.should_be_basket_total_message(product_price)

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()