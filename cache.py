import json
import os
from bs4 import BeautifulSoup
import requests
import re

class cache:

    def read_cache(self,CACHE_FNAME):
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


    def write_cache(self,cache_file, cache_dict):       
        json_cache = json.dumps(cache_dict)
        f = open(cache_file + ".json", 'w')
        f.write(json_cache)
        f.close()
