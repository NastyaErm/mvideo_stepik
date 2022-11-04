from selenium.webdriver import Keys
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class All_goods_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    checkbox_apple = "//a[contains(text(),'Ноутбуки Apple MacBook ')]"
    price = "//input[@class='range__price ng-star-inserted']"
    processor_menu = "//mvid-icon[@class='accordion__toggle-icon ng-tns-c202-12']"
    processor = "//a[contains(text(),' Apple M1 Pro ')]"

    # Getters
    def get_checkbox_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_apple)))

    def min_price(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def proc_menu(self):
        self.driver.execute_script("window.scrollBy(0, 500);") #скролл
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_menu)))

    def proc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor)))

        # Actions
    def checkbox_apple_click(self):
        self.get_checkbox_apple().click()
        print("Нажали на чекбокс")

    def input_min_price(self): #указываем диапазон цены
        self.min_price().click()
        self.min_price().send_keys(100000)
        self.min_price().send_keys(Keys.RETURN)
        print("Ввели мин. цену")

    def proc_menu_click(self):
        self.proc_menu().click()
        print("Нажали на меню типа процессора ")

    def proc_click(self):
        self.proc().click()
        print("Выбрали процессор Apple M1 Pro")