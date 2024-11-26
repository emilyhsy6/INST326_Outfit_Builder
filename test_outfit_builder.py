import unittest
import main_outfit_builder

#define test class(change method name
class TestStringMethods(unittest.TestCase):
#1.Create any data or objects needed for the test
#2.Call the function, method, or class you’re testing using the setup data
#3. Use assertions to verify that the output or behavior matches your expectations
#Example
class test_weather(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
