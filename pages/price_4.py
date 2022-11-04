from selenium.common import TimeoutException
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Price(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_in_cart = "//a[@class='cart-item__name ng-star-inserted']"
    button_make_order = "//button[@class='cart-total__button-total ng-tns-c294-1 mv-main-button--large mv-main-button--primary mv-button mv-main-button']"
    credit = "//span[@class='cart-total__credit-content ng-star-inserted']"

    def product_cart(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.product_in_cart)))
            print("Выбранный товар в корзине")
        except TimeoutException:
            print("Товара в корзине нет ")

        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))
            print("Можно оформить заказ, кнопка Перейти к оформлению кликабельна")
        except TimeoutException:
            print("Заказ оформить нельзя,кнопка Перейти к оформлению неактивна ")

        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.credit)))
            print("Кнопка В рассрочку или кредит кликабельна")
        except TimeoutException:
            print("Кнопка В рассрочку или кредит неактивна ")



