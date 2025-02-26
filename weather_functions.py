
def print_weather_data(weather):
    """Formats and prints weather data in a unified way
    for both the api calls and the database calls"""
    if isinstance(weather, dict):
        # If it's a dictionary (API data), extract weather data
        print(f"Min Temp: {weather['temp_min']}°C, Max Temp: {weather['temp_max']}°C, "
              f"Feels Like: {weather['feels_like']}°C, Pressure: {weather['pressure']} hPa, "
              f"Wind Speed: {weather['wind_speed']} m/s")
    elif isinstance(weather, tuple):
        # If it's a tuple (database data), extract weather data from the tuple
        print(f"Min Temp: {weather[2]}°C, Max Temp: {weather[3]}°C, Feels Like: {weather[4]}°C, "
              f"Pressure: {weather[5]} hPa, Wind Speed: {weather[6]} m/s")
    else:
        print("Invalid weather data format.")
