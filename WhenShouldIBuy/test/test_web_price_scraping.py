import unittest
import sys

sys.path.append("..")
import web_price_scraping


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_choose_premium_price_ok(self):
        self.assertEqual(web_price_scraping.choose(456), 4)

    def test_choose_premium_price_fail(self):
        self.assertNotEqual(web_price_scraping.choose(456), 5)

    def test_choose_premium_price_raise_type_error(self):
        with self.assertRaises(TypeError):
            web_price_scraping.choose('a')


if __name__ == '__main__':
    unittest.main()