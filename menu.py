from api_requests import get_weather_data
from weather_functions import print_weather_data
from database import find_city_data, insert_weather_data, show_weather_data, delete_weather_data, \
    delete_all_weather_data


def show_menu():
    """Displays the main menu"""
    print("\nWeather App Menu:")
    print("1) Show all stored current weather data")
    print("2) Enter a city name to see current weather data")
    print("3) Quit")


def handle_options():
    """Handles user choices in the menu"""
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_show_weather_data()
        elif choice == 2:
            handle_show_city_weather()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def get_user_choice():
    """Get and validate user choice."""
    try:
        choice = int(input("Choose an option (1/2/3): "))
        if choice not in [1, 2, 3]:
            raise ValueError("Choice must be 1, 2, or 3.")
        return choice
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid choice (1, 2, or 3).")
        return -1

def handle_show_weather_data():
    """Handles the display of all weather data in the database."""
    show_weather_data()
    delete_option = input("Do you want to delete data for:\n (a) Specific city, (b) All data, (c) No: ").lower()

    if delete_option== 'a':
        city_to_delete = input("Enter city to delete: ").lower()
        delete_weather_data(city_to_delete)
    elif delete_option == 'b':
        delete_all_weather_data()
    elif delete_option == 'c':
        print("No data deleted.")
    else:
        print("Invalid input. No data deleted.")

def handle_show_city_weather():
    """Handles the showing of weather data for a specific city."""
    city = str(input("Enter the city to show current weather for: ")).lower()
    city_data, weather_data = find_city_data(city)

    if city_data is None:
        print(f"City '{city}' not found in the database. Searching online...")
        weather = get_weather_data(city)
        if weather:
            print(f"\nWeather data for {city}:")
            print_weather_data(weather)
            save = input("Do you want to save this data to the database? (y/n): ").lower()
            if save == 'y':
                insert_weather_data(city, weather)
            else:
                print("Weather data was not saved.")
        else:
            print("Error retrieving weather data. Please try again later.")


    else:
        print(f"City '{city}' found in the database.")
        print_weather_data(weather_data)
        update = str(input("Do you want to update the data? (y/n): ")).lower()
        if update == 'y':
            lat, lon = get_geo_data(city)
            if lat and lon:
                weather = get_weather_data(lat, lon)
                if weather:
                    insert_weather_data(city, weather)
        elif update == 'n':
            print("Weather data remains unchanged.")
        else:
            print("Invalid input. Data remains unchanged.")
