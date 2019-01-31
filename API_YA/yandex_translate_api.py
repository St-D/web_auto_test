#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

import requests
import unittest

from param import *


def setUpModule():
    print("In setUpModule()")


def tearDownModule():
    print("In tearDownModule()")


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('======== case start ========')
        pass

    def tearDown(self):
        print('======== case end ========')
        pass

    def test_case_01(self):
        """Test supported languages"""
        print('#01 --', self.id())

        param_dict = {
            "key": KEY,
            "ui": None,
        }

        for lang_id, lang_name in LANG_ID.items():

            with self.subTest(lang_name=lang_name):
                param_dict['ui'] = lang_id
                res = requests.post(API_URL, data=param_dict)

                self.assertEqual(res.status_code, 200,
                                 'Status code is not OK for {}!'.format(lang_name))

                self.assertEqual(len(res.json()['langs']), len(LANG_ID),
                                 'List of supported languages is not complete for {}'.format(lang_name))


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # python -m test_cases.py -v


