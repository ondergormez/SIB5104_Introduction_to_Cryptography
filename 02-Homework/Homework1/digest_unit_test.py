import unittest

import digest


class TestDigest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass method called!")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass method called!")

    def setUp(self):
        print('setUp method called!')

    def tearDown(cls):
        print("tearDown method called!")

    def test_calculate_digest(self):
        print("Test calculate_digest() function starting...")

        message = "KRIPTOGRAFI"
        self.assertEqual(digest.Digest.calculate_digest(message), 64)

        print("Test calculate_digest() function finished successfully!")


if __name__ == '__main__':
    unittest.main()
