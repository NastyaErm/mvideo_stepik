from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    chapter = "//a[contains(text(),' Ноутбуки')]" #выбранный раздел

    def get_chapter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chapter)))

    def click_chapter(self):
        self.get_chapter().click()
        print("Нажали на раздел")

