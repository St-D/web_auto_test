#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

import unittest
import pytest
import allure
import time

from allure.constants import AttachmentType
from selenium import webdriver
from page import *

PATH_TO_DRIVER = "../drv/chromedriver.exe"
# PATH_TO_DRIVER = "../drv/geckodriver_0.23_x86.exe"
START_URL = "https://www.travelocity.com/"


# def setUpModule(set_index=None):
def setUpModule():
    # print(set_index)
    # path_to_drv = "../drv/chromedriver.exe"
    # driver_index = webdriver.Chrome(executable_path=path_to_drv)
    # driver_index.get("https://www.travelocity.com/")

    print("In setUpModule()")


def tearDownModule():
    print("In tearDownModule()")


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=PATH_TO_DRIVER)
        # cls.driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)
        cls.driver.get(START_URL)
        cls.hotel_name_on_chosen_page = None
        print(cls.driver.title)


        # cls.dataset = dataset
        # print(cls.dataset)
        # cls.btn_name = BTN

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        pass

    def setUp(self):
        time.sleep(1)
        # print('======== case start ========')
        pass

    def tearDown(self):
        time.sleep(1)
        # print('======== case end ========')
        pass

    @pytest.allure.step("Ввод исходных данных на странице")
    def test_case_01(self):
        """input data on main page"""

        print('#01 --', self.id())
        # load main page:
        main_page = MainPage(driver=self.driver)

        # checks title:
        assert main_page.is_title_matches(), "Page title doesn't match."

        main_page.select_car_flex()
        main_page.select_hotel_flex()

        main_page.input_town_area()

        main_page.input_date_check_in()
        main_page.input_date_check_out()

        main_page.click_search_btn()

        # test btn color:
        # self.assertEqual(btn_color, BTN_COLOR, 'color does not match expected')

    @pytest.allure.step("Выбор отеля среди найденных")
    def test_case_02(self):
        """select hotel"""
        print('#02 --', self.id())

        hotel_sel_page = HotelSelectPage(driver=self.driver)

        # checks title:
        assert hotel_sel_page.is_title_matches(), "Page title doesn't match."

        hotel_sel_page.select_hotel()

    @pytest.allure.step("Резервирование отеля/ проверка резервирования ранеевыбранного отеля")
    def test_case_03(self):
        """chosen hotel"""
        print('#03 --', self.id())

        chosen_hotel_page = ChosenHotelPage(driver=self.driver)

        self.hotel_name_on_chosen_page = chosen_hotel_page.get_hotel_name()
        # print(self.hotel_name_on_chosen_page)

        chosen_hotel_page.press_reserve_first()
        chosen_hotel_page.press_reserve_second()
        chosen_hotel_page.press_float_win_btn()

        # payment page test
        pay_page = PaymentPage(driver=self.driver)

        # print(pay_page.get_hotel_name())
        self.assertIn(str(self.hotel_name_on_chosen_page), str(pay_page.get_hotel_name()), "the hotel chosen is wrong")



if __name__ == '__main__':
    unittest.main(verbosity=2)
    # python test_cases.py -v

    # -------------------------------- cmd allure
    # Run: python -m pytest test_cases.py --alluredir ./res_allure #встроенный логер при этом не работает!
    # Show_report: allure serve ./res_allure/
    # Gen_report : allure generate -c -o rep_allure res_allure
    # Gen_report_2 : allure generate -c -o dir_to dir_from (-c -> clean, -o - by default allure-report)
    # -------------------------------- cmd allure


