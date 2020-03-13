import unittest
import main
import random_test


class TestMain(unittest.TestCase):
    # Like beforeEach() we see in JavaScript tests
    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        """test with number"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "hello"
        result = main.do_stuff(test_param)
        self.assertIsInstance(
            result, ValueError
        )  # checking if result is an instance of ValueError

    def test_for_none(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def test_for_empty(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    # after every test
    def tearDown(self):
        print("cleaning up mess")


class TestRandom(unittest.TestCase):
    def test_input(self):
        result = random_test.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = random_test.run_guess(5, 9)
        self.assertFalse(result)

    def test_input_out_of_range(self):
        result = random_test.run_guess(5, 19)
        self.assertFalse(result)

    def test_input_wrong_typw(self):
        result = random_test.run_guess(5, "5")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()  # not refering to the main.py file

