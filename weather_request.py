import requests
import json
import pandas as pd


def get_weather_data(lat, lon, time, key):
    """
    Request weather data from the dark_sky API.
    The key must be obtained from the official website. 

    """
    lat = str(lat)
    lon = str(lon)
    time = str(time)
    time = pd.to_datetime(time,infer_datetime_format=True).timestamp()
    time = int(time)
    api_key = str(key)
    querystring = {"lang":"en","units":"si"}
    url = "https://api.darksky.net/forecast/%s/%s,%s,%s?exclude=minutely,hourly,daily,alerts,flags" % (api_key, lat, lon, time)
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    data = data['currently']
    
    return_items = ['precipIntensity', 'precipProbability', 'temperature', 'apparentTemperature', 'dewPoint', 'humidity', 'windSpeed', 'windBearing', 'cloudCover', 'uvIndex', 'visibility'] # Declaring the variables
    return_data = [data.get(item) for item in return_items]  # Helps to prevent unknown values (if doesn't found cloudCover, just puts null)
    
    return return_data


