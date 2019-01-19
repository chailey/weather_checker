import unittest
from weather_checker import weather_checker_testing



class WeatherCheckerTests(unittest.TestCase):
    def test_pass_1(self):
        print("User input: chicago... ")
        self.assertEqual(weather_checker_testing("chicago"), "Passed")

    def test_pass_2(self):
        print("User input: Chicago...")
        self.assertEqual(weather_checker_testing("Chicago"), "Passed")
    def test_pass_3(self):
        print("User input: Chicago, IL...")
        self.assertEqual(weather_checker_testing("Chicago, IL"), "Passed")
    def test_pass_4(self):
        print("User input: Los Angeles...")
        self.assertEqual(weather_checker_testing("Los Angeles"), "Passed")
    def test_pass_5(self):
        print("User input: Los Angeles, USA")
        self.assertEqual(weather_checker_testing("Los Angeles, USA"), "Passed")
    def test_pass_6(self):
        print("User input: Los Angeles, CA")
        self.assertEqual(weather_checker_testing("Los Angeles, CA"), "Passed")
    def test_pass_7(self):
        print("User input: beijing...")
        self.assertEqual(weather_checker_testing("beijing"), "Passed")

    def test_fail_1(self):
        print("User input: asdf... ")
        self.assertEqual(weather_checker_testing("asdf"), "Failed")
    def test_fail_2(self):
        print("User input: -1...")
        self.assertEqual(weather_checker_testing("-1"), "Failed")
    def test_fail_3(self):
        print("User input: Chicago IL...")
        self.assertEqual(weather_checker_testing("Chicago IL"), "Failed")
    def test_fail_4(self):
        print("User input: Los anglez")
        self.assertEqual(weather_checker_testing("Los anglez"), "Failed")
    def test_fail_5(self):
        print("User input: Southern California")
        self.assertEqual(weather_checker_testing("Southern California"), "Failed")
    def test_fail_6(self):
        print("User input: 北京")
        self.assertEqual(weather_checker_testing("北京"), "Failed")
    def test_fail_7(self):
        print("User input: ILoveDWOLLA")
        self.assertEqual(weather_checker_testing("ILoveDWOLLA"), "Failed")

if __name__ == '__main__':
    unittest.main(verbosity=2)