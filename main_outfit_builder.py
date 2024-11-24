import argparse
import sys
import requests
import json
import config

def get_main():
    base = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London" #later integrate city input into argparse
    api_url = base + "appid=" + config.key + "&q=" + city + "&units=imperial"
    
    fetch_response = requests.get(api_url)
    response = fetch_response.json()
    
    if response["cod"] != "404":
        return response["main"]
    
main = get_main()

def get_weather():
    base = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London" #later integrate city input into argparse
    api_url = base + "appid=" + config.key + "&q=" + city + "&units=imperial"
    
    fetch_response = requests.get(api_url)
    response = fetch_response.json()
    
    if response["cod"] != "404":
        return response["weather"]

weather = get_weather()

def get_wind():
    base = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London" #later integrate city input into argparse
    api_url = base + "appid=" + config.key + "&q=" + city + "&units=imperial"
    
    fetch_response = requests.get(api_url)
    response = fetch_response.json()
    
    if response["cod"] != "404":
        return response["wind"]
    
wind = get_wind()

class Weather:
    def __init__(self):
        self.current_temp = main["temp"]
        self.high_temp = main["temp_max"]
        self.low_temp = main["temp_min"]
        self.humidity = main["humidity"]
        self.wind_speed = wind["speed"]
        self.description = weather[0]["description"]

    def __repr__(self):
        return_str = ""   

        return_str += f'Current Temperature: {self.current_temp} degrees F \nHigh Temperature: {self.high_temp} degrees F \nLow Temperature: {self.low_temp} degrees F'
        return_str += f'\nHumidity: {self.humidity}%'
        return_str += f'\nWind Speed: {self.wind_speed}'
        return_str += f'\nWeather is: {self.description}'
        
        return return_str

test = Weather()
print(test)

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
    # holidays = get_holidays(args.countrycode, args.year)