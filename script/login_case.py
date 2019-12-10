import unittest

from utils import DriverUtil


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
