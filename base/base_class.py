class Base():
    def __init__(self, driver):
        self.driver = driver


    #проверим урл:
    def get_current_url(self):  # метод,с помощью которого получаем url на котором в данный момент находимся в браузере
        get_url = self.driver.current_url
        print("current url " + get_url)