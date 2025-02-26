import sqlite3
from weather_functions import print_weather_data


def start_db():
    """Connect to the database and create tables if they don't exist."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    # Create tables if they don't exist
    c.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            city TEXT,
            main_weather TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS daily_weather (
            id INTEGER PRIMARY KEY,
            city TEXT UNIQUE, -- for when updating/deleting data
            min_temp REAL,
            max_temp REAL,
            feels_like REAL,
            pressure REAL,
            wind_speed REAL,
            FOREIGN KEY (city) REFERENCES cities(city)
        )
    """)

    conn.commit()
    conn.close()


def show_weather_data():
    """Show all weather data from the database."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cities")
    cities = c.fetchall()

    if cities:
        print("\nStored Current Weather Data :")
        for city in cities:
            print(f"City: {city[1]}, Main Weather: {city[2]}")
            c.execute("SELECT * FROM daily_weather WHERE city = ?", (city[1],))
            weather_data = c.fetchone()
            if weather_data:
                if weather_data:
                    weather_dict = {
                        'temp_min': weather_data[2],
                        'temp_max': weather_data[3],
                        'feels_like': weather_data[4],
                        'pressure': weather_data[5],
                        'wind_speed': weather_data[6]
                    }
                    print_weather_data(weather_dict)
                print()
    else:
        print("No weather data found in the database.")
    conn.close()


def find_city_data(city):
    """Search for city in the database and return data."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cities WHERE city = ?", (city,))
    city_data = c.fetchone()

    if city_data:
        c.execute("SELECT * FROM daily_weather WHERE city = ?", (city,))
        weather_data = c.fetchone()
        conn.close()
        return city_data, weather_data
    else:
        conn.close()
        return None, None


def insert_weather_data(city, weather):
    """Insert or update weather data for a city."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    # Insert city data if it doesn't exist
    c.execute("SELECT * FROM cities WHERE city = ?", (city,))
    if not c.fetchone():
        c.execute("INSERT INTO cities (city, main_weather) VALUES (?, ?)",
                  (city, weather['weather_main']))

    # Insert or update weather data
    c.execute('''
        INSERT INTO daily_weather (city, min_temp, max_temp, feels_like, pressure, wind_speed)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(city) DO UPDATE SET
            min_temp = excluded.min_temp,
            max_temp = excluded.max_temp,
            feels_like = excluded.feels_like,
            pressure = excluded.pressure,
            wind_speed = excluded.wind_speed
    ''', (city, weather['temp_min'], weather['temp_max'], weather['feels_like'],
          weather['pressure'], weather['wind_speed']))

    conn.commit()
    conn.close()


def delete_weather_data(city):
    """Delete a specific city weather data from the database."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('DELETE FROM daily_weather WHERE city = ?', (city,))
    c.execute('DELETE FROM cities WHERE city = ?', (city,))
    print(f"Weather for {city} removed from the database!")
    conn.commit()
    conn.close()


def delete_all_weather_data():
    """Delete all weather data from the database."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('DELETE FROM daily_weather')
    c.execute('DELETE FROM cities')
    print(f"All data was removed from the database - bet you are sorry now!")
    conn.commit()
    conn.close()
