import unittest
from main_outfit_builder import get_weather_data, Weather, Outfit
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
        self.weather = Weather(self.test_data["main"], self.test_data["wind"], self.test_data["weather"])
        
    def test_get_weather_data(self):
        """Assert that output data matches data pulled from API.
        """
        weather = get_weather_data(self.city)
        if weather:
            self.assertIn("main", weather)#Check if main data key exists in response
            self.assertIn("wind", weather)#Check if wind data exists response
            self.assertIn("weather", weather)#Check if weather exists response
        else:
            self.assertIsNone(weather,"City not found")   #return none
    
    def test_Weather(self):
        """Assert that Weather intitializes and displays correctly.
        """
        self.assertEqual(self.weather.current_temp, 45.0)
        self.assertEqual(self.weather.high_temp, 47.0)
        self.assertEqual(self.weather.low_temp, 41.0)
        self.assertEqual(self.weather.humidity, 80)
        self.assertEqual(self.weather.wind_speed, 6.0)
        self.assertEqual(self.weather.description, "overcast clouds")

        expected_repr = (
            "Current Temperature: 45.0 degrees F\n"
            "High Temperature: 47.0 degrees F\n"
            "Low Temperature: 41.0 degrees F\n"
            "Humidity: 80% (Humid)\n"
            "Wind Speed: 6.0 mph\n"
            "Weather is: overcast clouds"
        )
        self.assertEqual(repr(self.weather), expected_repr)
    
    def test_Outfit(self):
        """Assert that Outfit ouput is correct based on weather data.
        """
        outfit = Outfit(self.weather, None, None, None, None)

        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()
    
        self.assertEqual(outfit.top_layers, 2)
        self.assertEqual(outfit.bottom_layers, 1)
        self.assertEqual(outfit.materials, "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey")
        self.assertFalse(outfit.rain_protection)

if __name__ == '__main__':
    unittest.main()