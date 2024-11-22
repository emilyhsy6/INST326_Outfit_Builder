import argparse
import sys
import requests
import json

def get_weather():
    base = "http://api.openweathermap.org/data/2.5/weather?"
    key = "ad7391750b602b79e722687ca4960538"
    city = "London" #later integrate city input into argparse
    api_url = base + "appid=" + key + "&q=" + city
    
    fetch_response = requests.get(api_url)
    response = fetch_response.json()
    
    if response["cod"] != "404":
        return response["main"]
    
main = get_weather()

class City:
    def __init__(self, city):
        self.city = city
        
class Temperature(City):
    def __init__(self, city, current_temp, high_temp, low_temp):
        super().__init__(city)
        
        self.current_temp = current_temp
        self.high_temp = high_temp
        self.low_temp = low_temp

    
    '''Class with different functions to read the current temperature status of the user’s city
    '''
    def read_high():
        ''' Retrieve the highest temperature forecasted for the day 
        Returns: 
	        Float: The highest temperature in degrees Fahrenheit
        '''
    def read_low(): 
        ''' Retrieve the lowest temperature forecasted for the day 
        Return: 
	        Float: The lowest temperature in degrees Fahrenheit
        '''
    def read_average():
        ''' Calculate the average temperature forecasted for the day 
        Return: 
	        Float: The average temperature in degrees Fahrenheit
        '''
    def read_humidity():
        ''' Retrive the humidity level forecasted for the day 
        Return: 
	        Float: The humidity level in percentage
        '''
    def read_wind_speed():
        '''Retrive the wind speed forecasted for the day 
        Return: 
	        Float: The wind speed in mph
        '''


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
