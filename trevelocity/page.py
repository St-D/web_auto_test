#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

import logging
from locators import *


def web_loger(func):
    """ LOGER """
    def wrapper(self, *argv, **kwargv):

        logging.basicConfig(filename='web.log',
                            filemode="w",
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.info(func.__doc__)
        return func(self, *argv, **kwargv)

    return wrapper


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.main_page = MainPageLocators(driver=self.driver)

    @web_loger
    def is_title_matches(self):
        """сравнение имени сайта"""
        return "Travelocity" in self.driver.title

    @web_loger
    def select_car_flex(self):
        """сначала нажмем на FLEX car"""
        element = self.main_page.car_flex_btn
        element.click()

    @web_loger
    def select_hotel_flex(self):
        """нажмемем на нужный нам FLEX с выбором отеля"""
        element = self.main_page.hotel_flex_btn
        element.click()

    @web_loger
    def input_town_area(self):
        """ввод поиска города"""
        element = self.main_page.dest_input_text_area
        element.send_keys('Japantown, San Francisco')
        element.send_keys(Keys.DOWN)

    @web_loger
    def input_date_check_in(self):
        """ввод даты отправления"""
        check_in_data = self.main_page.input_date_check_in
        check_in_data.clear()
        check_in_data.send_keys('02/01/2019')

    @web_loger
    def input_date_check_out(self):
        """ввод даты возвращения"""
        check_out_data = self.main_page.input_date_check_out
        check_out_data.clear()

        for i in range(11):
            check_out_data.send_keys(Keys.BACK_SPACE)

        check_out_data.send_keys('02/15/2019')

    @web_loger
    def click_search_btn(self):
        """клик кнопки поиска"""
        search_btn = self.main_page.search_btn
        search_btn.click()


class HotelSelectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.select_page = HotelSelectPageLocators(driver=self.driver)

    def is_title_matches(self):
        return "Japantown" in self.driver.title

    def select_hotel(self):
        element = self.select_page.hotel
        element.click()


class ChosenHotelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.chosen_hotel = ChosenHotelLocators(driver=self.driver)

    def is_title_matches(self):
        return "" in self.driver.title

    def get_hotel_name(self):
        return self.chosen_hotel.hotel_name

    def press_reserve_first(self):
        element = self.chosen_hotel.reserve_btn_first
        element.click()

    def press_reserve_second(self):
        for x_p in self.chosen_hotel.reserve_btn_second:
            try:
                x_path = By.XPATH, x_p
                btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(x_path))
                # print(x_p)
                btn.click()
            except TimeoutException:
                continue

    def press_float_win_btn(self):
        for x_p in self.chosen_hotel.float_win_btn:
            try:
                x_path = By.XPATH, x_p
                # x_path = By.CSS_SELECTOR, x_p
                fl_win_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(x_path))
                fl_win_btn.click()
            except TimeoutException:
                continue


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_page = PaymentLocators(driver=self.driver)

    def get_hotel_name(self):
        return self.payment_page.hotel_name



# used for debugging only
def main():

    path_to_drv = "../drv/chromedriver.exe"
    driver_index = webdriver.Chrome(executable_path=path_to_drv)
    driver_index.get("https://www.travelocity.com/")

    print(driver_index.title)

    # -----------------------------------
    main_page_instant = MainPage(driver=driver_index)
    main_page_instant.select_car_flex()
    main_page_instant.select_hotel_flex()

    main_page_instant.input_town_area()

    main_page_instant.input_date_check_in()
    main_page_instant.input_date_check_out()

    main_page_instant.click_search_btn()

    # -----------------------------------
    hotel_sel_page = HotelSelectPage(driver=driver_index)
    hotel_sel_page.select_hotel()

    # -----------------------------------
    chosen_hotel_page = ChosenHotelPage(driver=driver_index)
    print(chosen_hotel_page.get_hotel_name())
    chosen_hotel_page.press_reserve_first()
    chosen_hotel_page.press_reserve_second()
    chosen_hotel_page.press_float_win_btn()

    # -----------------------------------
    pay_page = PaymentPage(driver=driver_index)
    print(pay_page.get_hotel_name())



if __name__ == '__main__':
    main()
    input()