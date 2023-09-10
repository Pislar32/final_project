import datetime
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    """Создан класс родитель Base - базовый"""

    """Метод инициализации"""
    def __init__(self, web_driver):
        self.driver = web_driver
        self.wait = WebDriverWait(self.driver, 15)


    """Метод создания скриншота"""
    def screen(self):
        new_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'screen' + new_date + '.png'
        self.driver.save_screenshot("D:\\QA_обучение\\Final_Project_DZ\\screenshots" + name_screen)
        print("screen Ok")

    """Метод парсинга и проверки слов"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("assert word Ok")

    """Метод проверки текущей url c url на странице"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("assert url Ok")

    """Метод получения текущей url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)
