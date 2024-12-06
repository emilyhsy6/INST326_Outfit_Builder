import argparse
import sys
import requests
import json
import config

def get_weather_data(city):
    """Get data from weather API
    
    Args:
        city (str): the weather data being retrieved for this city  

    Returns:
        dict: the weather data taken from the api
    """
    base = "http://api.openweathermap.org/data/2.5/weather?"
    api_url = base + "appid=" + config.key + "&q=" + city + "&units=imperial"

    fetch_response = requests.get(api_url)
    response = fetch_response.json()

    if response["cod"] != "404":
        return {
            "main": response["main"],
            "weather": response["weather"],
            "wind": response["wind"]
        }
    else:
        print(f"{city} not found.")
        return None

class Weather:
    def __init__(self, main_data, wind_data, weather_data):
        """Initialize the Weather class.
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
         return_str = ""   

         return_str += f"Current Temperature: {self.current_temp} degrees F"
         return_str += f"\nHigh Temperature: {self.high_temp} degrees F"
         return_str += f"\nLow Temperature: {self.low_temp} degrees F"
         return_str += f"\nHumidity: {self.humidity}%"
         return_str += f"\nWind Speed: {self.wind_speed}"
         return_str += f"\nWeather is: {self.description}"
        
         return return_str

class Outfit:
    """Class that determines the various outfit elements based on the weather
    """
    def __init__(self, parsed_weather, top_layers, bottom_layers, materials, rain_protection):
        self.parsed_weather = parsed_weather
        self.top_layers = top_layers
        self.bottom_layers = bottom_layers
        self.materials = materials
        self.rain_protection = rain_protection

    def decide_top_layers(self):
        """Decide how many layers the user should wear on top
        """
        if parsed_weather.low_temp <= 32:
            self.top_layers = 3
        elif parsed_weather.low_temp > 32 and parsed_weather.low_temp <= 60:
            self.top_layers = 2
        else:
            self.top_layers = 1
    
    def decide_bottom_layers(self):
        """Decide how many layers the user should wear on the bottom
        """
        if parsed_weather.low_temp <= 32:
            self.bottom_layers = 2
        else:
            self.bottom_layers = 1
            
    def decide_materials(self):
        """Decide what kind of fabric materials the user should wear
        """
        if parsed_weather.humidity <= 55:
            self.materials = "Cotton, Polyester, Wool, Silk, Denim, Leather, Cashmere, or Fleece"
            
        elif parsed_weather.humidity > 55:
            self.materials = "Cotton, Polyester, Linen, Silk, Rayon, Nylon, or Jersey"

    def decide_rain_protection(self):
        """Decide if the user should bring rain protection
        """
        if "rain" in parsed_weather.description:
            self.rain_protection = True
        else:
            self.rain_protection = False
            
    def __repr__(self):
        """Return string representation of Outfit class
        """
        return_str = ""
        
        return_str += f"\nWe recommend wearing {self.top_layers} layer(s) on top "
        return_str += f"and {self.bottom_layers} layer(s) on the bottom."
        return_str += f"\nThe recommended materials are {self.materials}."
        if self.rain_protection == True:
            return_str += f"\nDon't forget an umbrella!"
        else:
            return_str += f"\nHave a great day!"
        
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
    args = parser.parse_args(args_list)
    return args

if __name__ == "__main__":
    """
    Call the ... function
    """
    args = parse_args(sys.argv[1:])    
    weather = get_weather_data(args.cityname)
    
    if weather:
        main_data = weather["main"]
        weather_data = weather["weather"]
        wind_data = weather["wind"]

        parsed_weather = Weather(main_data, wind_data, weather_data)
        print(parsed_weather)
        
        outfit = Outfit(parsed_weather, None, None, None, None)
        outfit.decide_top_layers()
        outfit.decide_bottom_layers()
        outfit.decide_materials()
        outfit.decide_rain_protection()
        
        print(outfit)