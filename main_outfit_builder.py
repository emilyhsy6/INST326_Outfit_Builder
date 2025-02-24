import argparse
import sys
import requests

def get_weather_data(city, api_key):
    """Get data from weather API
    
    Args:
        city (str): the input city for which the weather data will be retrieved

    Returns:
        response (dict): the weather data retrieved from the API
    """
    base = "http://api.openweathermap.org/data/2.5/weather?"
    api_url = base + "appid=" + api_key + "&q=" + city + "&units=imperial"

    # Fetch response from the API
    fetch_response = requests.get(api_url)
    response = fetch_response.json()

    # If the city is found, extract relevant data
    if response["cod"] != "404":
        return {
            "main": response["main"],
            "weather": response["weather"],
            "wind": response["wind"]
        }
        
    # Print a message if the input City is not found
    else:
        print(f"{city} not found.") 
        return None

class Weather:
    """Class that determines the weather
    """
    def __init__(self, main_data, wind_data, weather_data):
        """Initialize the Weather class.

        Args:
            main_data (dict): Contains temperature and humidity data
            wind_data (dict): Holds wind speed data
            weather_data (list): Holds a description of the weather
        """
        self.current_temp = main_data["temp"]
        self.high_temp = main_data["temp_max"]
        self.low_temp = main_data["temp_min"]
        self.humidity = main_data["humidity"]
        self.wind_speed = wind_data["speed"]
        self.description = weather_data[0]["description"]

    def __repr__(self):
        """Return string represenation of Weather class.
        """
        # Initialize an empty string for output
        return_str = ""   

        # Build the output string with weather details
        return_str += f"Current Temperature: {self.current_temp} degrees F"
        return_str += f"\nHigh Temperature: {self.high_temp} degrees F"
        return_str += f"\nLow Temperature: {self.low_temp} degrees F"
        if self.humidity <= 55:
           return_str += f"\nHumidity: {self.humidity}% (Comfortable)"
        else:
           return_str += f"\nHumidity: {self.humidity}% (Humid)"
           return_str += f"\nWind Speed: {self.wind_speed} mph"
           return_str += f"\nWeather: {self.description}"
        
        # Return output string
        return return_str

class Outfit:
    """Class that determines the various outfit elements based on the weather
    """
    def __init__(self, parsed_weather, top_layers, bottom_layers, materials, rain_protection):
        """Initialize the Outfit class with weather data and outfit attributes

        Args:
            parsed_weather (Weather): The weather data
            top_layers (int): Recommended number of top layers to wear
            bottom_layers (int): Recommended number of bottom layers to wear
            materials (str): Recommended clothing materials to wear
            rain_protection (bool): Whether rain protection is needed for the day
        """
        self.parsed_weather = parsed_weather
        self.top_layers = top_layers
        self.bottom_layers = bottom_layers
        self.materials = materials
        self.rain_protection = rain_protection

    def decide_top_layers(self):
        """Decide how many layers the user should wear on top
        """
        # Maximum layers for very cold weather
        if self.parsed_weather.low_temp <= 32:
            self.top_layers = 3 
            
        # Moderate layers for cool weather
        elif self.parsed_weather.low_temp > 32 and self.parsed_weather.low_temp <= 60:
            self.top_layers = 2 
            
        # Single layer for warm weather
        else:
            self.top_layers = 1 
    
    def decide_bottom_layers(self):
        """Decide how many layers the user should wear on the bottom
        """
        # Maximum bottom layers for cold weather
        if self.parsed_weather.low_temp <= 32:
            self.bottom_layers = 2 
            
        # Single layer for other conditions
        else:
            self.bottom_layers = 1
            
    def decide_materials(self):
        """Decide what kind of fabric materials the user should wear
        """
        # Thicker materials for moderate to low humidity
        if self.parsed_weather.humidity <= 55:
            self.materials = "Cotton, Polyester, Wool, Silk, Denim, Leather, Cashmere, or Fleece"
            
        # Breathable materials for high humidity
        elif self.parsed_weather.humidity > 55:
            self.materials = "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey"

    def decide_rain_protection(self):
        """Decide if the user should bring rain protection
        """
        # Rain protection required
        if "rain" in self.parsed_weather.description:
            self.rain_protection = True
            
        # Rain protection not required
        else:
            self.rain_protection = False
            
    def __repr__(self):
        """Return string representation of Outfit class
        """
        # Initialize an empty string for output
        return_str = ""
        
        # Build the output string with outfit details
        return_str += f"\nWe recommend wearing {self.top_layers} layer(s) on top "
        return_str += f"and {self.bottom_layers} layer(s) on the bottom."
        return_str += f"\nThe recommended materials are {self.materials}."
        if self.rain_protection == True:
            return_str += f"\nDon't forget an umbrella!"
        else:
            return_str += f"\nHave a great day!"
        
        # Return output string
        return return_str

def parse_args(args_list):
    """ Parse command-line arguments.
    
    Args:
        args_list (list): the list of strings from the command prompt
        
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser(description="Weather Parser")
    parser.add_argument("cityname", type=str, help="Path to the directory containing city name")
    parser.add_argument("apikey", type=str, help="API key for weather API")
    args = parser.parse_args(args_list)
    return args

if __name__ == "__main__":
    """
    Main entry point for the script
    """
    # Parse command-line arguments and fetch weather data for the input city
    args = parse_args(sys.argv[1:])    
    weather = get_weather_data(args.cityname, args.apikey)
    
    if weather:
        main_data = weather["main"]
        weather_data = weather["weather"]
        wind_data = weather["wind"]

        # Create Weather object from retrieved data
        parsed_weather = Weather(main_data, wind_data, weather_data)
        print(parsed_weather)
        
        # Create Outfit object and decide recommendations
        outfit = Outfit(parsed_weather, None, None, None, None)
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()
        
        # Print outfit suggestions 
        print(outfit)