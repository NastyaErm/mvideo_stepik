from base.base_class import Base


class First_main_page(Base):

    url = "https://www.mvideo.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def first_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
