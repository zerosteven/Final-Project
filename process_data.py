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
        air_quality_data = self.cache.read_cache(cachefile2)
        chance_of_rain_data = self.cache.read_cache(cachefile3)
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table1} (id TEXT PRIMARY KEY, temp INTEGER)")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table2} (id TEXT PRIMARY KEY, )")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table3} (id TEXT PRIMARY KEY, )")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table4} (id TEXT PRIMARY KEY, )")
        for item in temp_data:
            id = item
            temp = temp_data[item]
            cur.execute(
                f"INSERT OR IGNORE INTO {self.table1} (id, temp) VALUES (?,?)", (id, temp))    