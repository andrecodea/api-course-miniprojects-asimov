import os
import requests
from pprint import pprint
import dotenv
import streamlit as st


def make_request(url, params=None):
    """
    Makes an HTTP GET request to the specified URL with optional parameters.
    
    Args:
        url (str): The URL to make the request to
        params (dict, optional): Query parameters for the request
    
    Returns:
        dict or None: JSON response data if successful, None if error occurs
    """
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()  # Raises HTTPError for bad responses
    except requests.HTTPError as e:
        print(f"Request error --> {e}")
        result = None
    else:
        result = response.json()  # Parse JSON response
    return result


def get_weather_for_location(location):
    """
    Fetches weather data for a specific location using OpenWeatherMap API.
    
    Args:
        location (str): City name to get weather data for
    
    Returns:
        dict or None: Weather data dictionary if successful, None if error occurs
    """
    # Load environment variables from .env file
    dotenv.load_dotenv()
    
    # Get API token from environment variables
    api_token = os.environ['CHAVE_API_OPENWEATHER']
    
    # OpenWeatherMap API endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # API request parameters
    params = {
        'appid': api_token,        # API authentication key
        'q': location,             # City name query
        'units': 'metric',         # Temperature in Celsius
        'lang': 'pt_br',          # Language for weather descriptions
    }
    
    # Make API request and return weather data
    weather_data = make_request(url=url, params=params)
    return weather_data


def main():
    """
    Main function that creates the Streamlit web interface for the weather app.
    Displays weather information including temperature, humidity, and cloud coverage.
    """
    # App title and data source information
    st.title('Weather Web App')
    st.write('OpenWeather data source: https://api.openweathermap.org/data/2.5/weather')
    
    # User input for city name
    location = st.text_input('Search for a city:')
    
    # Stop execution if no location is provided
    if not location:
        st.stop()
    
    # Fetch weather data for the specified location
    weather_data = get_weather_for_location(location=location)
    
    # Handle case when no data is found
    if not weather_data:
        st.warning(f'No data found for city {location.capitalize()}')
        st.stop()
    
    # Extract weather information from API response
    current_weather = weather_data['weather'][0]['description']  # Weather description
    temperature = weather_data['main']['temp']                   # Current temperature
    feels_like = weather_data['main']['feels_like']             # Feels like temperature
    humidity = weather_data['main']['humidity']                  # Humidity percentage
    cloud_coverage = weather_data['clouds']['all']              # Cloud coverage percentage
    
    # Display main weather condition
    st.metric(label=f'Current weather in {location.capitalize()}', 
              value=current_weather.capitalize())
    
    # Create two columns for organized metric display
    col1, col2 = st.columns(2)
    
    # Left column: Temperature metrics
    with col1:
        st.metric(label=f'Temperature in {location.capitalize()}', 
                  value=f'{temperature} °C')
        st.metric(label=f'Feels like in {location.capitalize()}', 
                  value=f'{feels_like} °C')
    
    # Right column: Environmental metrics
    with col2:
        st.metric(label=f'Humidity in {location.capitalize()}', 
                  value=f'{humidity}%')
        st.metric(label=f'Cloud coverage in {location.capitalize()}', 
                  value=f'{cloud_coverage}%')


if __name__ == '__main__':
    main()