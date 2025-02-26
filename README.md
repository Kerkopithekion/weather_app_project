# weather_app_project
~~Basic version of current weather app~~~

A very simple version of an application that shows current weather - description, minimum temperature, maximum temperature, 'feels like' temperature, pressure, and wind speed. 
The data is saved for a specific city. 

App logic:

User is show a basic menu, prompted to either see all current stored data, search by entering the name of a specific city, or quit. 
When viewing data, user has the option to delete - individual city data, or all data.
When searching by city, the app first looks for data in the database and displays it if it exists. 
If it does not exist, it calls the apis - first the latitude and longitude data is generated from city name, and then the weather data is returned. 
User then has the option to save it into the database (if not exist) or update it (if exists.)

Note: the api_key variable needs to be input before the code will run as designed. 

Possible future updates:

Better user interface, especially with the update option. 
Break down into more smaller logical functions in the menu.py file.
Add 'are you sure' step when deleting.
Testing. 
Some error handling done, but not unified throughout the code. More informative error handling would be helpful in the api calls.
Check that all casting is done and unified throughout the code. 
