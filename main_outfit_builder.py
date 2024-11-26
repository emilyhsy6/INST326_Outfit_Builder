import argparse
import sys
import requests
import json
import config

def get_weather_data(city):
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
        self.current_temp = main_data["temp"]
        self.high_temp = main_data["temp_max"]
        self.low_temp = main_data["temp_min"]
        self.humidity = main_data["humidity"]
        self.wind_speed = wind_data["speed"]
        self.description = weather_data[0]["description"]

    def __repr__(self):
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
    def __init__(self, layers, materials, lengths, rain_protection):
        self.layers = layers
        self.materials = materials
        self.lengths = lengths
        self.rain_protection = rain_protection

    def decide_layers():
        """Decide how many layers the user should wear
        """
    def decide_materials():
        """Decide what kind of fabric materials the user should wear
        """
    def decide_sleeve_or_pant_length():
        """Decide what length of clothes the user should wear
        """

def output_weather():
    """Call the ReadTemp class and display attributes as cohesive statement
    """
    
def output_outfit():
    """Call the Outfit class and display attributes as cohesive statement
    """
    
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