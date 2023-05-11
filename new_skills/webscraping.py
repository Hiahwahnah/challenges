import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(filename='scraping.log', level=logging.INFO)

def scrape_weather_data(url):
    try:
        # Send request to the website
        response = requests.get(url)

        # Check for successful response
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find weather data elements
        temperature_elements = soup.find_all("span", class_="temperature")
        date_elements = soup.find_all("span", class_="date")

        # Extract data
        dates = [date.text for date in date_elements]
        temperatures = [float(temp.text.strip().split()[0]) for temp in temperature_elements]

        # Store data in a DataFrame
        weather_data = pd.DataFrame({"Date": dates, "Temperature": temperatures})

        return weather_data

    except Exception as e:
        logging.exception("Error occurred while scraping weather data:")
        raise e

def plot_temperature_data(weather_data):
    plt.plot(weather_data["Date"], weather_data["Temperature"])
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather Data")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # Set the URL to scrape
    url = "https://www.accuweather.com/"

    # Scrape weather data
    try:
        weather_data = scrape_weather_data(url)

        # Perform basic analysis
        print(weather_data.head())

        # Plot temperature data
        plot_temperature_data(weather_data)

    except Exception as e:
        print("An error occurred during scraping and analysis.")
        logging.exception("Error occurred during scraping and analysis:")