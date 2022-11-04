import time
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Filters(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    show_all_filters_button = "//div[@class='ng-tns-c233-3 ng-trigger ng-trigger-fadeInOut ng-star-inserted']"
    scaner = "//a[contains(text(),' Сканер отпечатка пальца ')]"
    found_goods_button = "//button[@class='button button--full-size ng-star-inserted']"
    first_good = "(//div[@class='product-card--list__description']//div[@class='product-title product-title--list'])[1]"
    cart_catalog = "(//mvid-button[@class='cart-button button_without-icon']//button[@title='Добавить в корзину'])[1]"
    cart = "//div[@class='nav-tab tab-cart']"

    # Getters

    def show_all_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_filters_button)))

    def select_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scaner)))

    def found_goods(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.found_goods_button)))

    def first_item_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_good)))

    def cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_catalog)))

    def main_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions

    def show_all_filters_click(self):
        self.show_all_filters().click()
        print("Нажимаем на кнопку Показать все фильтры")

    def select_filters_click(self):
        self.select_filters().click()
        print("Выбрали фильтр Отпечаток пальца")

    def found_goods_click(self):
        self.found_goods().click()
        print("Показали все найденные товары")

    def first_item_list_print(self):
        self.cart_button().click()
        time.sleep(3)
        print("Добавили в корзину первый найденный товар")

    def main_basket_click(self):
        self.main_basket().click()
        print("Перешли в корзину")

