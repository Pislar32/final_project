import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Main_pade(Base):
    """Класс главная страница"""
    """Класс Login page стал потомком класса Base"""


    # LOCATORS - ЛОКАТОРЫ


    base_url = "https://www.wildberries.ru/"
    button_catalog = "//button[@class='nav-element__burger j-menu-burger-btn j-wba-header-item hide-mobile']"
    electronics_section = "//li[@data-menu-id='4830']"
    pop_up_menu_laptops_and_computers = "//span[text()='Ноутбуки и компьютеры']"
    pop_up_laptops = "//a[text()='Ноутбуки']"
    main_word = "//h1[@class='catalog-title']"




    # GETTERS - ПОЛУЧАЕМ


    def get_button_catalog(self):
        """Метод вызывает переменную button_catalog"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))
    print("get_button_catalog Ok")

    def get_electronics_section(self):
        """Метод вызывает переменную electronics_section"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.electronics_section)))
    print("get_electronics_section Ok")

    def get_pop_up_menu_laptops_and_computers(self):
        """Метод вызывает переменную pop_up_menu_laptops_and_computers"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pop_up_menu_laptops_and_computers)))
    print("get_pop_up_menu_laptops_and_computers Ok")

    def get_pop_up_laptops(self):
        """Метод вызывает переменную pop_up_laptops"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pop_up_laptops)))
    print("get_pop_up_laptops Ok")

    def get_main_word(self):
        """Метод get_main_word парсит слово - Ноутбуки и ультрабуки на странице Ноутбуки и ультрабуки, для подтверждение перехода"""
        return self.wait.until(EC.invisibility_of_element((By.XPATH, self.main_word)))
    print("get_main_word Ok")


    # ACTIONS - ДЕЙСТВИЯ


    def click_button_catalog(self):
        """Метод кликает на кнопку главное меню"""
        self.get_button_catalog().click()
        print("get_button_catalog Ok")

    def click_electronics_section(self):
        """Метод кликает на кнопку раздел ЭЛЕКТРОНИКА"""
        action = ActionChains(self.driver)
        element = self.get_electronics_section()
        action.move_to_element(element).perform()
        print("click_electronics_section Ok")

    def click_pop_up_menu_laptops_and_computers(self):
        """Метод кликает на всплывающее меню ноутбуки и компьютеры"""
        self.get_pop_up_menu_laptops_and_computers().click()
        print("click_pop_up_menu_laptops_and_computers Ok")

    def click_pop_up_laptops(self):
        """Метод кликает на раздел ноутбуки"""
        self.get_pop_up_laptops().click()
        print("click_pop_up_laptops Ok")



    # METHOD - МЕТОД


    def select_menu_about(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(1.2)
        self.click_button_catalog()
        time.sleep(3)
        self.click_electronics_section()
        time.sleep(3)
        self.click_pop_up_menu_laptops_and_computers()
        time.sleep(2)
        self.click_pop_up_laptops()
        self.assert_url("https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki")











