import unittest
from main_outfit_builder import get_weather_data, Weather, Outfit
from unittest.mock import patch

class TestOutfitBuilder(unittest.TestCase):
    """ Testing outfit builder program, API retrieval, weather object, and logic for outfit suggestions.
    """ 
    def setUp(self):
        """ Set up test data and initialize sample data for testing.
        """      
        # Set up mock data for tests
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
    
    @patch('main_outfit_builder.requests.get')
    def test_get_weather_data(self, mock_get):
        """Test get_weather_data function and ensure that the correct keys are pulled from API
        """
        # Mock the API response
        mock_response = {
            "cod": 200,  # Simulates a successful API call
            "main": self.test_data["main"],
            "wind": self.test_data["wind"],
            "weather": self.test_data["weather"]
        }

        # Configure the mock to return the response when json() is called
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # Call the function
        weather = get_weather_data(self.city, "dummy_api_key")
        
        # Assertions
        self.assertIsNotNone(weather)
        self.assertIn("main", weather)
        self.assertIn("wind", weather)
        self.assertIn("weather", weather)
        self.assertEqual(weather["main"]["temp"], 45.0)
    
    def test_Weather(self):
        """Test the initialization of the Weather class and ensure it's returning the correct strings.
        """
        # Assertions 
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
            "Weather: overcast clouds"
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
        
        # Expected string representation of the Outfit class
        expected_repr = (
            "\nWe recommend wearing 2 layer(s) on top and 1 layer(s) on the bottom.\n"
            "The recommended materials are Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey.\n"
            "Have a great day!"
        )
        self.assertEqual(repr(outfit), expected_repr)
        
    def test_Outfit_rainy_weather(self):
        """Test Outfit class logic for rainy weather
        """
        rainy_weather_data = {
            "main": {
                "temp": 50.0,
                "temp_max": 55.0,
                "temp_min": 48.0,
                "humidity": 65,
            },
            "wind": {
                "speed": 10.0,
            },
            "weather": [
                {"description": "light rain"}
            ]
        }
        rainy_weather = Weather(rainy_weather_data["main"], rainy_weather_data["wind"], rainy_weather_data["weather"])
        outfit = Outfit(rainy_weather, None, None, None, None)

        # Run decision-making process 
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()

        # Verify outfit suggestions 
        self.assertEqual(outfit.top_layers, 2)
        self.assertEqual(outfit.bottom_layers, 1)
        self.assertEqual(outfit.materials, "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey")
        self.assertTrue(outfit.rain_protection)

    def test_Outfit_extreme_cold(self):
        """Test Outfit class logic for extremely cold weather
        """
        cold_weather_data = {
            "main": {
                "temp": 10.0,
                "temp_max": 15.0,
                "temp_min": 5.0,
                "humidity": 30,
            },
            "wind": {
                "speed": 15.0,
            },
            "weather": [
                {"description": "clear sky"}
            ]
        }
        cold_weather = Weather(cold_weather_data["main"], cold_weather_data["wind"], cold_weather_data["weather"])
        outfit = Outfit(cold_weather, None, None, None, None)

        # Run decision-making process 
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()

        # Verify outfit suggestions 
        self.assertEqual(outfit.top_layers, 3)
        self.assertEqual(outfit.bottom_layers, 2)
        self.assertEqual(outfit.materials, "Cotton, Polyester, Wool, Silk, Denim, Leather, Cashmere, or Fleece")
        self.assertFalse(outfit.rain_protection)

if __name__ == '__main__':
    unittest.main()