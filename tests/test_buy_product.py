from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.laptops_and_ultrabooks_page import Laptops_and_ultrabooks_pade
from pages.main_page import Main_pade
from pages.product_page_acer import Product_page_acer


def test_buy_product():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path=r"D:\QA_обучение\Chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)

    """Импорт класса Main_pade"""
    mp = Main_pade(driver)
    mp.select_menu_about()

    """Импорт класса Laptops_and_ultrabooks_pade"""
    lup = Laptops_and_ultrabooks_pade(driver)
    lup.select_menu_about()

    """Импорт класса Product_page_acer"""
    pps = Product_page_acer(driver)
    pps.select_product()

    """Импорт класса Product_page_acer"""
    cp = Cart_page(driver)
    cp.making_an_order()
















