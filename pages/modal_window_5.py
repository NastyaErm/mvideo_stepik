from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

class Modal_exit(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    button_make_order = "//button[@class='cart-total__button-total ng-tns-c294-1 mv-main-button--large mv-main-button--primary mv-button mv-main-button']"
    entry_field = "//input[@id='mvideo-form-field-input-0']"
    modal_window = "//mvid-icon[@class='login-form-top-nav__btn-icon']"
    delete_button = "//a[@class='cart-list__delete-selected-button mv-link-button--default mv-button mv-link-button ng-star-inserted']"
    empty_cart = "//div[@class='cart-empty']"

    def make_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))

    def number_entry(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entry_field)))

    def delete_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))



    def make_order_click(self):
        self.make_order().click()
        print("Нажали на кнопку Перейти к оформлению ")

    def entering_phone_number(self, number):
        self.number_entry().send_keys(number)
        print("Номер введен")

    def close_modal_window(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.modal_window))).click()
        print("Модальное окно закрыто")

    def delete_product_click(self):
        self.delete_product().click()
        print("Товары из корзины удалены")

    def cart_is_empty(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.empty_cart)))
            print("Корзина очищена")
        except TimeoutException:
            print("Корзина не очищена")
