#before operating this code kindly make sure to add install the "requests" module using the "pip install requests" 
import requests 
import json

# Constants
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'
FAVORITES_FILE = 'favorites.txt'

# Function to fetch weather data from OpenWeatherMap
def fetch_weather_data(location):
    params = {'q': location, 'appid': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Function to fetch weather forecast
def fetch_weather_forecast(location):
    params = {'q': location, 'appid': API_KEY}
    response = requests.get(FORECAST_URL, params=params)
    data = response.json()
    return data

# Function to save favorite locations
def save_favorite(location):
    with open(FAVORITES_FILE, 'a') as file:
        file.write(location + '\n')

# Function to load favorite locations
def load_favorites():
    try:
        with open(FAVORITES_FILE, 'r') as file:
            favorites = [line.strip() for line in file]
        return favorites
    except FileNotFoundError:
        return []

# Main loop
def main():
    favorites = load_favorites()

    while True:
        print("\nOptions:")
        print("1. Fetch Weather Data")
        print("2. Fetch Weather Forecast")
        print("3. Save Favorite Location")
        print("4. View Favorite Locations")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            location = input("Enter location: ")
            weather_data = fetch_weather_data(location)
            print(json.dumps(weather_data, indent=4))
        
        elif choice == '2':
            location = input("Enter location: ")
            weather_forecast = fetch_weather_forecast(location)
            print(json.dumps(weather_forecast, indent=4))
        
        elif choice == '3':
            location = input("Enter location to save as favorite: ")
            save_favorite(location)
        
        elif choice == '4':
            print("Favorite Locations:")
            for i, location in enumerate(favorites, 1):
                print(f"{i}. {location}")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
