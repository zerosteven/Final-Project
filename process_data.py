import sqlite3
import json
import os
import numpy as np
from matplotlib import pyplot as plt
from sqlite3.dbapi2 import SQLITE_SELECT
from cache import cache

class process_data:
    

    def __init__(self, db_name, table1, table2,table3,table4):
        
        self.cache = cache()
        self.db_name = db_name
        self.table1 = table1
        self.table2 = table2
        self.table3 = table3
        self.table4 = table4

    def setUpDatabase(self):
        path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(path+'/'+ self.db_name + '.db')
        cur = conn.cursor()
        return cur, conn

    def SetUpTable(self, cachefile1, cachefile2, cachefile3, cur, conn):

        temp_data = self.cache.read_cache(cachefile1)
        wind_speed_in_miles_data = self.cache.read_cache(cachefile2)
        humidity_data = self.cache.read_cache(cachefile3)
        #pressureInches
        #temperature,windspeedMiles, humidity,visibility.
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table1} (id TEXT PRIMARY KEY, temperature INTEGER)")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table2} (id TEXT PRIMARY KEY, wind_speed_in_miles INTEGER)")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table3} (id TEXT PRIMARY KEY, pressure_per-inches INTEGER,)")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table4} (id TEXT PRIMARY KEY, humidity INTEGER, visibility INTEGER)")
        
        for item in temp_data:
            id = item
            temperature = temp_data[item]
            cur.execute(
                f"INSERT OR IGNORE INTO {self.table1} (id, temperature) VALUES (?,?)", (id, temperature))    
        
        for item in wind_speed_in_miles_data:
            id = item
            wind_speed_in_miles = wind_speed_in_miles_data[item]
            cur.execute(
                f"INSERT OR IGNORE INTO {self.table2} (id, wind_speed_in_miles) VALUES (?,?)", (id, wind_speed_in_miles))
        
        for item in humidity_data:
            id = item
            pressure_per-inches = humidity_data[item]["pressure_per-inches"]
            humidity = humidity_data[item]["humidity"]
            visibility = humidity_data[item["visibility"]]
            cur.execute(
                f"INSERT OR IGNORE INTO {self.tb_name_3} (id, pressure_per-inches) VALUES (?,?)", (id, pressure_per-inches))
            cur.execute(
                f"INSERT OR IGNORE INTO {self.tb_name_4} (id, humidity,visibility) VALUES (?,?,?)", (id, humidity,visibility))
        #use JOIN and fulfill the requirement(where tempeature is negative)
        cur.execute('DELETE FROM humidity_data WHERE humidity_data.id IN (SELECT humidity_data.id FROM humidity_data JOIN temp_data ON temp_data.id = humidity_data.id WHERE temp_data.temperature <= 0)')
        conn.commit()

