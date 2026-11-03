from pages.basket_page import BasketPage
from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()