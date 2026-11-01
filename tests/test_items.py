from selenium.webdriver.common.by import By

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_displayed_on_product_page(browser):
    browser.get(LINK)
    # time.sleep(30)  # раскомментируйте для проверки языка, см. ниже
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) == 1, "Кнопка добавления в корзину не найдена на странице товара"