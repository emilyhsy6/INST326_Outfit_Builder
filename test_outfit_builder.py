import unittest
import argparse
import json
from main_outfit_builder import get_weather_data, Weather, Outfit, parse_args
class TestOutfitBuilder(unittest.TestCase):
    def create_test_data(self):
        self.test_data = {
            "main": {
                "temp": 45.0,
                "temp_max": 47.0,
                "temp_min": 41.0,
                "humidity": 80,
            },
            "wind": {
                "speed": 6.0,
            },
            "weather": [
                {"description": "overcast clouds"}
            ]
        }
        self.city = "London"
        
    def test_get_weather_data(self):
        """Assert that output data matches data pulled from API.
        """
        weather = get_weather_data(self)
        if weather:
            self.assertIn("main", weather)#Check if "main" data key exists in response
            self.assertIn("wind", weather)#Check if "wind" key exists response
            self.assertIn("weather", weather)#Check if "weather" key exists response
        else:
            self.assertIsNone(weather,"City not found")   #return none
    
    def test_Weather(self):
        """Assert that output is correct and matches data pulled from API.
        """
    
    def test_Outfit(self):
        """Assert that ouput is correct based on weather data.
        """

if __name__ == '__main__':
    unittest.main()
