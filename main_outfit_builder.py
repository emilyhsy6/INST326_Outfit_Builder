import argparse
import sys
import requests
import json
import config

def get_weather():
    base = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London" #later integrate city input into argparse
    api_url = base + "appid=" + config.key + "&q=" + city
    
    fetch_response = requests.get(api_url)
    response = fetch_response.json()
    
    if response["cod"] != "404":
        return response["main"]
    
main = get_weather()

class Weather:
    def __init__(self,current_temp, high_temp, low_temp, humidity, wind_speed, precipitation):
        self.current_temp = current_temp
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.precipitation = precipitation

    def get_temps(self):
        self.current_temp = main["temp"]
        self.high_temp = main["temp_max"]
        self.low_temp = main["temp_min"]

    def get_humidity(self):
        self.humidity = main["humidity"]

    def get_windSpeed(self):
        self.wind_speed = main["speed"]

    def get_precipitation(self):
        self.precipitation = main["pop"] # probability percentage

    def __repr__(self):
        return_str = ""   

        return_str += f'Current Temperature: {self.current_temp} \nHigh Temperature: {self.high_temp} \nLow Temperature: {self.low_temp} \nHumidity: {self.humidity}
        '
        += f'Humidity: {self.humidity}'
        
class WindSpeed():
    
        
    def __repr__(self):
        return f'Wind Speed: {self.wind_speed}'
        
class Precipitation():

        
    def __repr__(self):
        return f'Probability Percentage of Precipitation: {self.precipitation}'


class Outfit:
    """Class that determines the various outfit elements based on the weather
    """
    def decide_outfit():
        """Decide the final outfit based on combination of elements
        """
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