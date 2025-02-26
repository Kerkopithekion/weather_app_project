import requests

api_key = '' # insert own api key!
geo_base_url = f"http://api.openweathermap.org/geo/1.0/direct"
# hardcoded to give the first answer if multiple options
weather_base_url = "https://api.openweathermap.org/data/2.5/weather"


def get_geo_data(city: str):
    geo_url = f"{geo_base_url}?q={city}&limit=1&appid={api_key}"
    try:
        response = requests.get(geo_url)

        if response.status_code == 200:
            data = response.json()

            if data:
                lat = data[0]['lat']
                lon = data[0]['lon']
                return lat, lon
            else:
                print(f"No data found for {city}.")
                return None, None

        else:
            print(f"Something went wrong! HTTP Status Code: {response.status_code}.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"The following error occurred: {e}")
        return None, None

def get_weather_data(city:str):

    lat, lon = get_geo_data(city)

    if lat and lon:
        weather_url = f"{weather_base_url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        try:
            response = requests.get(weather_url)

            if response.status_code == 200:
                data = response.json()
                weather_info = {
                    'weather_main': data['weather'][0]['main'],
                    'temp_min': data['main']['temp_min'],
                    'temp_max': data['main']['temp_max'],
                    'feels_like': data['main']['feels_like'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': data['wind']['speed'],
                }
                return weather_info
            else:
                print(f"Unable to get weather data!! HTTP Status Code: {response.status_code}.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"The following error occurred: {e}")
            return None
    else:
        print("Error retrieving geo data. Please try again later.")
        return None
