import time
import pytest
from selenium import webdriver
from pages.all_filters_3 import Filters
from pages.all_goods_page_2 import All_goods_page
from pages.first_main_page_1 import First_main_page
from pages.main_page import Main_page
from pages.price_4 import Price
from pages.modal_window_5 import Modal_exit


def test_buy_our_product():
    driver = webdriver.Chrome(executable_path="C:\\Users\\nastj\\resource\\chromedriver.exe")

    fp = First_main_page(driver)
    fp.first_page()
    time.sleep(5)

    gch = Main_page(driver)
    gch.get_chapter()
    gch.click_chapter()
    time.sleep(2)

    agp = All_goods_page(driver)
    agp.get_checkbox_apple()
    agp.checkbox_apple_click()

    agp.min_price()
    agp.input_min_price()
    time.sleep(3)

    agp.proc_menu()
    agp.proc_menu_click()

    agp.proc()
    agp.proc_click()
    time.sleep(2)

    f = Filters(driver)
    f.show_all_filters()
    f.show_all_filters_click()
    f.select_filters_click()
    f.found_goods_click()

    f.first_item_list()
    f.first_item_list_print()

    f.main_basket()
    f.main_basket_click()
    time.sleep(5)

    p = Price(driver)
    p.product_cart()

    me = Modal_exit(driver)
    me.make_order()
    me.make_order_click()
    me.number_entry()
    me.entering_phone_number("9999999999")
    me.close_modal_window()
    me.delete_product()
    me.delete_product_click()
    me.cart_is_empty()

    time.sleep(5)
    driver.quit()


