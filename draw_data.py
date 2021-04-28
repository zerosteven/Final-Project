from matplotlib import pyplot as plt
import json
import os
from bs4 import BeautifulSoup
import requests
import re
from cache import *
from ratelimit import limits, sleep_and_retry


API_KEY_temp = "bf4b8fabdbc444da93c141445212504"

# @sleep_and_retry
# @limits(calls=25, period=10)
def create_request_url_for_temp():
    # cache.read_cache()
    location = "Beijing"
    tp = "24" # default daily weather
    daterange = ["2021-01-01","2021-01-02","2021-01-03","2021-01-04","2021-01-05","2021-01-06","2021-01-07","2021-01-08","2021-01-09","2021-01-10","2021-01-11","2021-01-12","2021-01-13","2021-01-14","2021-01-15","2021-01-16","2021-01-17","2021-01-18","2021-01-19","2021-01-20","2021-01-21","2021-01-22","2021-01-23","2021-01-24","2021-01-25","2021-01-26","2021-01-27","2021-01-28","2021-01-29","2021-01-30","2021-01-31","2021-02-01","2021-02-02","2021-02-03","2021-02-04","2021-02-05","2021-02-06","2021-02-07","2021-02-08","2021-02-09","2021-02-10","2021-02-11","2021-02-12","2021-02-13","2021-02-14","2021-02-15","2021-02-16","2021-02-17","2021-02-18","2021-02-19","2021-02-20","2021-02-21","2021-02-22","2021-02-23","2021-02-24","2021-02-25","2021-02-26","2021-02-27","2021-02-28","2021-03-01","2021-03-02","2021-03-03","2021-03-04","2021-03-05","2021-03-06","2021-03-07","2021-03-08","2021-03-09","2021-03-10","2021-03-11","2021-03-12","2021-03-13","2021-03-14","2021-03-15","2021-03-16","2021-03-17","2021-03-18","2021-03-19","2021-03-20","2021-03-21","2021-03-22","2021-03-23","2021-03-24","2021-03-25","2021-03-26","2021-03-27","2021-03-28","2021-03-29","2021-03-30","2021-03-31","2021-04-01","2021-04-02","2021-04-03","2021-04-04","2021-04-05","2021-04-06","2021-04-07","2021-04-08","2021-04-09","2021-04-10","2021-04-11"]
    
    for x in daterange:
        start_date = x
        params = f"?q={location}&date={start_date}&key={API_KEY_temp}&tp={tp}&format=json"
        url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx" + params
        print(url)

        try:
            r = requests.get(url)
            print(f"Fetching data……")
            content = json.loads(r.text)
            content = content['data']['weather'][0]
            print(content)

            cache_dict = {}
            cache_dict['temp'] = int(content["avgtempC"])
            cache_dict['date'] = content['date']
            cache_dict['WindSpeed'] = content["hourly"][0]["windspeedMiles"]
            cache_dict['Pressure'] = content['hourly'][0]['pressure']
            cache_dict['Humidity'] = content['hourly'][0]['humidity']
            cache_dict['Visibility'] = content['hourly'][0]['visibility']
            print(cache_dict)
            cache.write_cache("weather", cache_dict)
            print("Data fetched\n--------------")
        except:
            print('Error when requesting url\n--------------')
            return None



def main():
    
    url = create_request_url_for_temp()
    print(url)

    # fetch_data_temp(cache_dict, url)

    # https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?aggregateHours=24&combinationMethod=aggregate&
    # startDateTime=2021-01-01T00%3A00%3A00&endDateTime=2021-04-11T00%3A00%3A00&maxStations=-1&maxDistance=-1&contentType=json&unitGroup=uk&locationMode=single&key=Y5MU9FU86GNMR536KG5ADX99S&dataElements=default&locations=Beijing

main()
