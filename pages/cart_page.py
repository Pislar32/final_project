import time
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart_page(Base):
    """Страница товара Acer"""


    # LOCATORS

    word_acer_cart = "//span[@class='good-info__good-name']"
    word_acer_price_cart = "//div[@class='list-item__price-new']"
    button_confirm_order = "//button[@name='ConfirmOrderByRegisteredUser']"
    # Кнопка подтверждения заказа

    # "//button[contains(@class, 'btn-main') and contains(text?(), 'Добавить в корзину')]" пойск xpath по двум параметрам




    # GETTERS


    def get_word_acer_cart(self):
        """Метод вызывает переменную word_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.word_acer_cart)))
    print("get_word_acer_cart Ok")

    def get_word_acer_price_cart(self):
        """Метод вызывает переменную word_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.word_acer_price_cart)))

    def get_button_confirm_order(self):
        """Метод вызывает переменную button_confirm_order"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_confirm_order)))
    print("get_button_confirm_order Ok")



    # ACTIONS


    def click_button_confirm_order(self):
        """Метод кликает и вызывает get_button_confirm_order"""
        self.get_button_confirm_order().click()
        print("click_button_confirm_order")



    # METHOD


    def making_an_order(self):
        self.get_current_url()
        self.assert_word(self.get_word_acer_cart(), "Ноутбук Acer Nitro 5 AN515-57 I785SGN (NH.QELER.005)")
        # self.assert_word(self.get_word_acer_price_cart(), "74576")
        time.sleep(1.5)
        self.click_button_confirm_order()
        time.sleep(0.5)
        self.screen()



