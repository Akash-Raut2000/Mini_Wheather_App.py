import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to fetch weather data. Please check your city name and API key.")

def main():
    print("Mini Weather App")
    city = input("Enter a city: ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    get_weather(city, api_key)

if __name__ == "__main__":
    main()