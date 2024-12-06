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

         return_str += f'Current Temperature: {self.current_temp} degrees F'
         return_str += f'\nHigh Temperature: {self.high_temp} degrees F'
         return_str += f'\nLow Temperature: {self.low_temp} degrees F'
         return_str += f'\nHumidity: {self.humidity}%'
         return_str += f'\nWind Speed: {self.wind_speed}'
         return_str += f'\nWeather is: {self.description}'
        
         return return_str

class Outfit:
    """Class that determines the various outfit elements based on the weather
    """
    def __init__(self, parsed_weather, top_layers, bottom_layers, materials, lengths, rain_protection):
        self.parsed_weather = parsed_weather
        self.top_layers = top_layers
        self.bottom_layers = bottom_layers
        self.materials = materials
        self.lengths = lengths
        self.rain_protection = rain_protection

    def decide_top_layers(self):
        """Decide how many layers the user should wear on top
        """
    def decide_materials():
        """Decide what kind of fabric materials the user should wear
        """
    def decide_lengths(self):
        """Decide what length of clothes the user should wear
        """
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
        
        return_str += f"We recommend wearing {self.top_layers} layer(s) on top "
        return_str += f"and {self.bottom_layers} layer(s) on the bottom"
        if self.rain_protection == True:
            return_str += f"\n Don't forget an umbrella!"
        else:
            return_str += f"\n Have a great day!"

def main():
    """Call the output functions and give user a final response
    """

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