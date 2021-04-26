from matplotlib import pyplot as plt
import json
import os
from bs4 import BeautifulSoup
import requests
import re

API_KEY_temp = "bf4b8fabdbc444da93c141445212504"
API_KEY_
API_KEY_

def read_cache(CACHE_FNAME):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FILE = dir_path + '/' + CACHE_FNAME + ".json"
    try:
        cache_file = open(CACHE_FILE, 'r', encoding="utf-8")
        cache_contents = cache_file.read()
        cache_list = json.loads(cache_contents)
        cache_file.close()
        return cache_list
    except:
        cache_list = {}
        return cache_list


def write_cache(cache_file, cache_dict):       
        json_cache = json.dumps(cache_dict)
        f = open(cache_file + ".json", 'w')
        f.write(json_cache)
        f.close()

def create_request_url_for_temp(date):
    location = "Beijing"
    tp = "24" # default daily weather
    
    params = f"?q={location}&date={date}&key={API_KEY_temp}&tp={tp}&format=json"
    url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx" + params
    return url

def fetch_data_temp(CACHE_FNAME,cache_dict, datetime, url):
    cache_dict = read_cache(CACHE_FNAME)
    
    r = requests.get(url)
    print(f"Fetching data for {datetime}")

    try:
        content = json.loads(r.text)
        cache_dict[datetime] = int(content["data"]["weather"][0]["avgtempC"])
        write_cache(CACHE_FNAME, cache_dict)
        print("Data fetched\n--------------")
    except:
        print('Error when requesting url\n--------------')
        return None