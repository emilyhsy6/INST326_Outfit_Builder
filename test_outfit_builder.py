import unittest
from main_outfit_builder import get_weather_data, Weather, Outfit

class TestOutfitBuilder(unittest.TestCase):
    """ Testing outfit builder program, which include API data retrival, weather object, and logic for outfit suggestions.
    """ 
    def setUp(self):
        """ Set up test data and initialize sample data for testing.
        """
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
        """Test get_weather_data function and ensure that the correct keys are pulled from API
        """
        weather = get_weather_data(self.city)
        if weather:
            self.assertIn("main", weather) # Check if main data key exists in response
            self.assertIn("wind", weather) # Check if wind data exists response
            self.assertIn("weather", weather) # Check if weather exists response
        else:
            self.assertIsNone(weather,"City not found") #return none
    
    def test_Weather(self):
        """Test the initialization of the Weather class and ensure it's returning the correct strings.
        """
        self.assertEqual(self.weather.current_temp, 45.0)
        self.assertEqual(self.weather.high_temp, 47.0)
        self.assertEqual(self.weather.low_temp, 41.0)
        self.assertEqual(self.weather.humidity, 80)
        self.assertEqual(self.weather.wind_speed, 6.0)
        self.assertEqual(self.weather.description, "overcast clouds")

        # Expected string representation of weather class
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
        """ Test the logic behind the outfit class for deciding bottom and top layers, clothing materials, and rain protection.
        """
        # Initialize outfit object with the test weather instance
        outfit = Outfit(self.weather, None, None, None, None)

        # Run decision-making process 
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()
    
        # Verify outfit suggestions 
        self.assertEqual(outfit.top_layers, 2)
        self.assertEqual(outfit.bottom_layers, 1)
        self.assertEqual(outfit.materials, "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey")
        self.assertFalse(outfit.rain_protection)

if __name__ == '__main__':
    unittest.main()