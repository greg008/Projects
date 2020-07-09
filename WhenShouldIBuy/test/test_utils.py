import sys
sys.path.append("..")
import unittest

import mock

import utils as ut


class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_choose_premium_price_ok(self):
        self.assertEqual(ut.choose(456.5), 4)

    def test_choose_premium_price_bounaries(self):
        self.assertEqual(ut.choose(400), 4)

    def test_choose_premium_price_fail(self):
        self.assertNotEqual(ut.choose(456), 5)

    def test_choose_premium_price_out_of_range(self):
        self.assertNotEqual(ut.choose(45), 5)

    def test_choose_premium_price_mock_else(self):
        with mock.patch('utils.choose', return_value='Begining price is not'
                                                     'in the correct range'):
            self.assertEqual(ut.choose(45),
                             'Begining price is not in the correct range')

    def test_choose_premium_price_raise_type_error(self):
        with self.assertRaises(TypeError):
            ut.choose('a')


if __name__ == '__main__':
    unittest.main()
