#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

from selenium.webdriver.common.by import By
from selenium import webdriver
# from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys

# from selene.browser import element


class MainPageLocators(object):
    """A class for main page locators"""

    def __init__(self, driver=None):
        self.driver = driver

    @property
    def hotel_flex_btn(self):
        x_path = By.XPATH, '//*[@id="tab-hotel-tab-hp"]'
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(x_path))

    @property
    def car_flex_btn(self):
        x_path = By.XPATH, '//*[@id="tab-car-tab-hp"]'
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(x_path))

    @property
    def dest_input_text_area(self):
        x_path = By.XPATH, '//input[@id="hotel-destination-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))
        # return x_path

    @property
    def input_date_check_in(self):
        x_path = By.XPATH, '//input[@id="hotel-checkin-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))

    @property
    def input_date_check_out(self):
        x_path = By.XPATH, '//input[@id="hotel-checkout-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))

    @property
    def room_number(self):
        x_path = By.XPATH, '//select[@id="hotel-rooms-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))

    @property
    def adult_number(self):
        x_path = By.XPATH, '//select[@id="hotel-rooms-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))

    @property
    def children_number(self):
        x_path = By.XPATH, '//select[@id="hotel-1-children-hp-hotel"]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(x_path))

    @property
    def search_btn(self):
        x_path = By.XPATH, '//*[@id="gcw-hotel-form-hp-hotel"]/div[8]/label/button'
        # x_path = By.XPATH, '//div[8]/label/button'
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(x_path))
        # return x_path


class HotelSelectPageLocators(object):
    """A class for select hotel locators"""

    def __init__(self, driver=None, hotel_num=2):
        self.driver = driver
        self.hotel_num = hotel_num

    @property
    def hotel(self):
        css_sel = By.CSS_SELECTOR, 'a.flex-link'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(css_sel))[self.hotel_num]

    @property
    def headr_title(self):
        return By.XPATH, './/div[2]/div/h1'


class ChosenHotelLocators(object):
    """A class for selected hotel locators"""
    def __init__(self, driver=None):
        self.driver = driver

    @property
    def hotel_name(self):
        x_path = By.XPATH, './/h1[@id="hotel-name"]'
        # yourtext = driver_index.find_element(By.TAG_NAME, 'h1')
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(x_path)).text

    @property
    def reserve_btn_first(self):
        x_path = By.XPATH, './/*[@id="mock-book-button"]'
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(x_path))

    @property
    def reserve_btn_second(self):
        return '//*[@id="rooms-and-rates"]/div/article/table/tbody[1]/tr/td[3]/div/div[1]/button', \
               '//*[@id="rooms-and-rates"]/div/article/table/tbody[1]/tr[1]/td[3]/div/form/div[1]/button',\
               '//*[@id="rooms-and-rates"]/div/article/table/tbody/tr/td[3]/div/div[1]/button',\

    @property
    def float_win_btn(self):
        return './/*[@id="deposit-pay-now-button"]',\
               './/*[@id="pay-now-button"]'
        # return '#deposit-pay-now-button'


class PaymentLocators(object):
    """A class for selected hotel locators"""
    def __init__(self, driver=None):
        self.driver = driver

    @property
    def hotel_name(self):
        # x_path = By.XPATH, './/body'
        x_path = By.XPATH, '//*[@id="trip-summary"]/div[1]/div[1]/div/figure/div[2]/h3/div/span'
        # yourtext = driver_index.find_element(By.TAG_NAME, 'h1')
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(x_path)).text


# used for debugging only
def main():
    # ------------------------main page
    path_to_drv = "../drv/chromedriver.exe"
    driver_index = webdriver.Chrome(executable_path=path_to_drv)
    driver_index.get("https://www.travelocity.com/")
    cl_instant = MainPageLocators(driver=driver_index)
    print(driver_index.title)
    # ------------------------

    # btn_car = driver_index.find_element(*cl_instant.car_flex_btn)
    # btn_car.click()

    btn_car = cl_instant.car_flex_btn.click()

    btn_h = cl_instant.hotel_flex_btn.click()


    # cl_instant.hotel_flex_btn.click()

    # btn_hotel = driver_index.find_element(cl_instant.hotel_flex_btn)
    # btn_hotel.click()


    input_town_area = cl_instant.dest_input_text_area
    input_town_area.send_keys('Japantown, San Francisco')
    input_town_area.send_keys(Keys.DOWN)
    # input_town_area.send_keys(Keys.ENTER)

    check_in_data = cl_instant.input_date_check_in
    check_in_data.clear()
    check_in_data.send_keys('01/28/2019')


    check_out_data = cl_instant.input_date_check_out
    check_out_data.clear()

    for i in range(15):
        check_out_data.send_keys(Keys.BACK_SPACE)

    check_out_data.send_keys('02/21/2019')


    # search_btnn = driver_index.find_element(*cl_instant.search_btn)
    search_btnn = cl_instant.search_btn
    search_btnn.click()
    # ------------------------

    # ------------------------
    cl_instant_hotel = HotelSelectPageLocators(driver=driver_index)
    h = cl_instant_hotel.hotel
    h.click()

    # ------------------------
    driver_index.switch_to.window(driver_index.window_handles[1])
    cl_instant_sel_hotel = ChosenHotelLocators(driver=driver_index)

    print(cl_instant_sel_hotel.hotel_name)

    r_b_f = cl_instant_sel_hotel.reserve_btn_first
    r_b_f.click()

    # ======
    for x_p in cl_instant_sel_hotel.reserve_btn_second:
        try:
            x_path = By.XPATH, x_p
            btn = WebDriverWait(driver_index, 15).until(EC.element_to_be_clickable(x_path))
            print(x_p)
            btn.click()
        except TimeoutException:
            continue
    # ======

    # ======
    for x_p in cl_instant_sel_hotel.float_win_btn:
        try:
            x_path = By.XPATH, x_p
            fl_win_btn = WebDriverWait(driver_index, 15).until(EC.element_to_be_clickable(x_path))
            fl_win_btn.click()
        except TimeoutException:
            continue
    # ======
    # ------------------------

    # ------------------------
    cl_instant_pay = PaymentLocators(driver=driver_index)
    print(cl_instant_pay.hotel_name)

    # ------------------------

if __name__ == '__main__':
    main()
    input()

