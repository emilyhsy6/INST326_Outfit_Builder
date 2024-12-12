import unittest
import argparse
import json
from main_outfit_builder import get_weather_data, Weather, Outfit, parse_args
class TestOutfitBuilder(unittest.TestCase):
    def setUp(self):
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
            self.assertIn("main", weather)#Check if main data key exists in response
            self.assertIn("wind", weather)#Check if wind data exists response
            self.assertIn("weather", weather)#Check if weather exists response
        else:
            self.assertIsNone(weather,"City not found")   #return none
    
    def test_Weather(self):
        """Assert that output is correct and matches data pulled from API.
        """
        """Test the Weather class initialization and representation."""
        weather = Weather(self.test_data["main"], self.test_data["wind"], self.test_data["weather"])
        self.assertEqual(weather.current_temp, 45.0)
        self.assertEqual(weather.high_temp, 47.0)
        self.assertEqual(weather.low_temp, 41.0)
        self.assertEqual(weather.humidity, 80)
        self.assertEqual(weather.wind_speed, 6.0)
        self.assertEqual(weather.description, "overcast clouds")

        expected_repr = (
            "Current Temperature: 45.0°F\n"
            "High Temperature: 47.0°F\n"
            "Low Temperature: 41.0°F\n"
            "Humidity: 80% (Humid)\n"
            "Wind Speed: 6.0 mph\n"
            "Weather Description: overcast clouds"
        )
        self.assertEqual(repr(weather), expected_repr)
    
    def test_Outfit(self):
        """Assert that ouput is correct based on weather data.
        """

        weather = Weather(self.test_data["main"], self.test_data["wind"], self.test_data["weather"])
        outfit = Outfit(weather)
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()
    
        self.assertEqual(outfit.decide_top_layers, 2)
        self.assertEqual(outfit.decide_bottom_layers, 1)
        self.assertEqual(outfit.decide_materials, "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey")
        self.assertFalse(outfit.decide_rain_protection)

        self.assertEqual

if __name__ == '__main__':
    unittest.main()
