from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # Сообщение "Товар добавлен в корзину" (первое сообщение)
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    # Сообщение со стоимостью корзины (третье сообщение)
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")