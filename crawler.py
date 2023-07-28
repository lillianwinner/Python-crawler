# Python News & Weather Crawler (NewsWeatherCrawler)

import requests
from bs4 import BeautifulSoup
import json

# Function to fetch Weather
def fetch_weather(location):
    weather_api = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': location, 'appid': 'my_api_key'}
    response = requests.get(weather_api, params=parameters)
    weather_data = response.json()
    return weather_data

# Function to fetch News
def fetch_news(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # Adjust this based on the website's structure
    return [headline.get_text() for headline in headlines]

# Driver function
def main():
    location = 'Los Angeles' # Change to the location you want
    weather_data = fetch_weather(location)

    # print(f"Weather in {location}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}K") # Adjust this line based on the API's response structure

    website_url = 'https://www.bbc.com/news' # Change to the news website you want
    news_data = fetch_news(website_url)
    print(f"Headlines from {website_url}:")
    for headline in news_data:
        print(headline)

if __name__ == "__main__":
    main()
