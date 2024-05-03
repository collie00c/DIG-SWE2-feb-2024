import requests

def get_city_coordinates(city):
    # API-Endpoint: "https://geocoding-api.open-meteo.com/v1/search"
    api_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city

    response = requests.get(api_url).json()
    return response


def get_weather_forecast(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(api_url).json()
    return response


# https://archive-api.open-meteo.com/v1/archive?latitude=52.52437&longitude=13.41053&start_date=2024-03-08&end_date=2024-03-08&daily=temperature_2m_max,temperature_2m_min


def get_weather_history(latitude, longitude, start_date, end_date):
    api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(api_url).json()
    return response




city = "Essen"
city_coordinates = get_city_coordinates(city)

# print(city_coordinates)


latitude = city_coordinates["results"][0]["latitude"]
longitude = city_coordinates["results"][0]["longitude"]

print(
    "The coordinates of",
    city,
    "are: longitude:",
    longitude,
    "and latitude:",
    latitude,
)

weather_forecast = get_weather_forecast(latitude, longitude)
print (weather_forecast)
time = weather_forecast["daily"]["time"]
print (time)


temperature_2m_min = weather_forecast["daily"]["temperature_2m_min"]
temperature_2m_max = weather_forecast["daily"]["temperature_2m_max"]

for i in range(len(time)):
    print(
        "The weather forecast for",
        city,
        "on",
        str(i)+': '+time[i],
        "is a minimum temperature of",
        temperature_2m_min[i],
        "and a maximum temperature of",
        temperature_2m_max[i],
    )




weather_date = "2019-03-08"
weather_history = get_weather_history(
    latitude=latitude,
    longitude=longitude,
    start_date=weather_date,
    end_date=weather_date,
)

historic_time = weather_history["daily"]["time"]
historic_temperature_2m_min = weather_history["daily"]["temperature_2m_min"]
historic_temperature_2m_max = weather_history["daily"]["temperature_2m_max"]

for i in range(len(historic_time)):
    print(
        "The temperatures in",
        city,
        "on",
        historic_time[i],': ',
        "Minimum temperature -> "+str(temperature_2m_min[i]),
        "Maximum temperature -> "+str(temperature_2m_max[i])        
    )
