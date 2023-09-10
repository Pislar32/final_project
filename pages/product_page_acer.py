import time
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product_page_acer(Base):
    """Страница товара Acer"""


    # LOCATORS

    word_acer = "//h1[text()='Ноутбук Acer Nitro 5 AN515-57 I785SGN (NH.QELER.005)']"
    word_acer_price = "//span[@class='price-block__final-price']"
    specifications_acer = "//a[@href='#options']"
    expand_description = "//button[@class='collapsible__toggle j-wba-card-item j-wba-card-item-show j-description-btn']"
    cart = "//a[@data-wba-header-name='Cart']"

    # "//button[contains(@class, 'btn-main') and contains(text?(), 'Добавить в корзину')]" пойск xpath по двум параметрам




    # GETTERS



    def get_word_acer(self):
        """Метод вызывает переменную word_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.word_acer)))
    print("get_word_acer Ok")

    def get_word_acer_price(self):
        """Метод вызывает переменную word_acer_price"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.word_acer_price)))
    print("get_word_acer_price Ok")

    def get_specifications_acer(self):
        """Метод вызывает переменную specifications_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.specifications_acer)))
    print("get_specifications_acer Ok")

    def get_expand_description(self):
        """Метод вызывает переменную expand_description"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.expand_description)))
    print("get_expand_description Ok")

    def scroll_up_product_page(self):
        """Скроллим вверх для видимости(визуальной) кнопки корзины"""
        self.driver.execute_script("window.scrollBy(0, -950)")
        print("scroll_up_product_page Ok")

    def get_cart(self):
        """Метод вызывает переменную cart"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    print("get_cart Ok")



    # ACTIONS


    def click_specifications_acer(self):
        """Метод вызывает и кликает на get_specifications_acer"""
        self.get_specifications_acer().click()
        print("click_specifications_acer Ok")

    def click_expand_description(self):
        """Метод вызывает и кликает на get_expand_description"""
        self.get_expand_description().click()
        print("click_expand_description Ok")

    def click_cart(self):
        """Метод вызывает и кликает на get_cart"""
        self.get_cart().click()
        print("click_cart Ok")



    # METHOD


    def select_product(self):
        self.get_current_url()
        self.assert_word(self.get_word_acer(), "Ноутбук Acer Nitro 5 AN515-57 I785SGN (NH.QELER.005)")
        # self.assert_word(self.get_word_acer_price(), "74576")
        time.sleep(2)
        self.click_specifications_acer()
        time.sleep(1)
        self.assert_url("https://www.wildberries.ru/catalog/134131268/detail.aspx")
        self.click_expand_description()
        time.sleep(1.5)
        self.scroll_up_product_page()
        time.sleep(2)
        self.click_cart()



