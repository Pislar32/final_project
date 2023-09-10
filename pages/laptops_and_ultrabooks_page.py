import time
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


class Laptops_and_ultrabooks_pade(Base):
    """Класс ноутбуки и ультрабуки"""


    # LOCATORS - ЛОКАТОРЫ


    filter_sorter = "//button[@class='dropdown-filter__btn dropdown-filter__btn--sorter']"
    filter_sorter_min_price = "//span[text()='По убыванию цены']"
    filter_brand = "//button[text()='Бренд']"
    filter_brand_acer = "//span[text()='Acer']"
    filter_brand_asus = "//span[text()='Asus']"
    button_done_brand = "//button[text()='Готово']"
    filter_vendor = "//button[text()='Продавец']"
    filter_vendor_wildberries = "//span[text()='Wildberries']"
    button_done_vendor = "//button[text()='Готово']"
    filter_price = "//button[text()='Цена, ₽']"
    filter_price_from = "//input[@name='startN']"
    filter_price_up_to = "//input[@name='endN']"
    button_done_price = "//button[text()='Готово']"
    move_computer_acer = "//a[@href='https://www.wildberries.ru/catalog/134131268/detail.aspx']"
    add_to_cart_acer = "//*[@id='c134131268']/div/div[3]/p[3]/a"
    select_product_acer = "//a[@href='https://www.wildberries.ru/catalog/134131268/detail.aspx']"




    # GETTERS - ПОЛУЧАЕМ


    def get_filter_sorter(self):
        """Метод вызывает переменную filter_sorter"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_sorter)))
    print("get_filter_sorter Ok")

    def get_filter_min_price(self):
        """Метод вызывает переменную filter_min_price"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_sorter_min_price)))
    print("get_filter_min_price Ok")

    def get_filter_brand(self):
        """Метод вызывает переменную filter_brand"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_brand)))
    print("get_filter_brand Ok")

    def get_filter_brand_acer(self):
        """Метод вызывает переменную filter_brand_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_acer)))
    print("get_filter_brand_acer Ok")

    def get_filter_brand_asus(self):
        """Метод вызывает переменную filter_brand_asus"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_asus)))
    print("get_filter_brand_asus Ok")

    def get_button_done_brand(self):
        """Метод вызывает переменную button_done_brand"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_done_brand)))
    print("get_button_done_brand Ok")

    def get_filter_vendor(self):
        """Метод вызывает переменную filter_vendor"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_vendor)))
    print("get_filter_vendor Ok")

    def get_filter_vendor_wildberries(self):
        """Метод вызывает переменную filter_vendor_wildberries"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_vendor_wildberries)))
    print("get_filter_vendor_wildberries Ok")

    def get_button_done_vendor(self):
        """Метод вызывает переменную button_done_vendor"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_done_vendor)))
    print("get_button_done_vendor Ok")

    def get_filter_price(self):
        """Метод вызывает переменную filter_price"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))
    print("get_filter_price Ok")

    def get_filter_price_from(self):
        """Метод вызывает переменную filter_price_from"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_price_from)))
    print("get_filter_price_from Ok")

    def get_filter_price_up_to(self):
        """Метод вызывает переменную filter_price_up_to"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_price_up_to)))
    print("get_filter_price_up_to Ok")

    def get_button_done_price(self):
        """Метод вызывает переменную button_done_price"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_done_price)))
    print("get_button_done_price Ok")

    def get_move_computer_acer(self):
        """Метод вызывает переменную move_computer_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.move_computer_acer)))
    print("get_select_computer_acer Ok")

    def get_add_to_cart_acer(self):
        """Метод вызывает переменную add_to_cart_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_acer)))
    print("get_add_to_cart_acer Ok")

    def get_select_computer_acer(self):
        """Метод вызывает переменную select_product_acer"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_product_acer)))
    print("get_select_computer_acer Ok")



    # ACTIONS - ДЕЙСТВИЯ


    def click_filter_sorter(self):
        """Метод вызывает и кликает на get_filter_sorter"""
        self.get_filter_sorter().click()
        print("click_filter_sorter Ok")

    def click_filter_min_price(self):
        """Метод вызывает и кликает на filter_min_price"""
        self.get_filter_min_price().click()
        print("click_filter_min_price Ok")

    def click_filter_brand(self):
        """Метод вызывает и кликает на filter_brand"""
        self.get_filter_brand().click()
        print("click_filter_brand Ok")

    def click_filter_brand_acer(self):
        """Метод вызывает и кликает на filter_brand_acer"""
        self.get_filter_brand_acer().click()
        print("click_filter_brand_acer Ok")

    def click_filter_brand_asus(self):
        """Метод вызывает и кликает на filter_brand_asus"""
        self.get_filter_brand_asus().click()
        print("click_filter_brand_asus Ok")

    def click_button_done_brand(self):
        """Метод вызывает и кликает на button_done_brand"""
        self.get_button_done_brand().click()
        print("click_button_done_brand Ok")

    def click_filter_vendor(self):
        """Метод вызывает и кликает на filter_vendor"""
        self.get_filter_vendor().click()
        print("click_filter_vendor Ok")

    def click_filter_vendor_wildberries(self):
        """Метод вызывает и кликает на get_filter_vendor_wildberries"""
        self.get_filter_vendor_wildberries().click()
        print("click_filter_vendor_wildberries Ok")

    def click_button_done_vendor(self):
        """Метод вызывает и кликает на get_button_done_vendor"""
        self.get_button_done_vendor().click()
        print("click_button_done_vendor Ok")

    def clicK_filter_price(self):
        """Метод вызывает и кликает на filter_price"""
        self.get_filter_price().click()
        print("clicK_filter_price")

    def input_filter_price_from(self):
        """Метод заполняет цену от filter_price_from"""
        self.get_filter_price_from().send_keys(Keys.CONTROL + 'A')
        self.get_filter_price_from().send_keys(Keys.BACKSPACE)
        time.sleep(1)
        self.get_filter_price_from().send_keys("21000")
        print("input_filter_price_from Ok")

    def input_filter_price_up_to(self):
        """Метод заполняет цену до filter_price_up_to"""
        self.get_filter_price_up_to().send_keys(Keys.CONTROL + 'A')
        self.get_filter_price_up_to().send_keys(Keys.BACKSPACE)
        self.get_filter_price_up_to().send_keys("90000")
        print("input_filter_price_up_to Ok")

    def click_button_done_price(self):
        """Метод вызывает и кликает на button_done_price"""
        self.get_button_done_price().click()
        print("click_button_done_price Ok")

    def scrooll_down_laptops_and_ultrabooks_pade(self):
        """Метод скролит страницу вниз"""
        self.driver.execute_script("window.scrollTo(0, 700)")
        print("scrooll_down_laptops_and_ultrabooks_pade Ok")

    def move_select_computer_acer(self):
        """Метод вызывает и кликает на get_select_computer_acer"""
        action = ActionChains(self.driver)
        element = self.get_move_computer_acer()
        action.move_to_element(element).perform()
        time.sleep(4)
        print("move_select_computer_acer Ok")

    def click_add_to_cart_acer(self):
        """Метод вызывает и кликает на get_add_to_cart_acer"""
        self.get_add_to_cart_acer().click()
        print("click_add_to_cart_acer Ok")

    def click_select_computer_acer(self):
        """Метод вызывает и кликает на select_product_acer"""
        self.get_select_computer_acer().click()
        print("click_get_select_computer_acer Ok")


    # METHOD - МЕТОД


    def select_menu_about(self):
        self.get_current_url()
        time.sleep(2)
        self.click_filter_sorter()
        time.sleep(1.5)
        self.click_filter_min_price()
        time.sleep(1.5)
        self.click_filter_brand()
        time.sleep(1.5)
        self.click_filter_brand_acer()
        time.sleep(1)
        self.click_filter_brand_asus()
        time.sleep(1)
        self.click_button_done_brand()
        time.sleep(1)
        self.click_filter_vendor()
        time.sleep(1)
        self.click_filter_vendor_wildberries()
        time.sleep(1)
        self.click_button_done_vendor()
        self.clicK_filter_price()
        time.sleep(1)
        self.input_filter_price_from()
        time.sleep(1)
        self.input_filter_price_up_to()
        time.sleep(1)
        self.click_button_done_price()
        time.sleep(2)
        self.scrooll_down_laptops_and_ultrabooks_pade()
        time.sleep(3)
        self.move_select_computer_acer()
        time.sleep(2)
        self.click_add_to_cart_acer()
        time.sleep(1.5)
        self.click_select_computer_acer()



