# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:27:00 2016

@author: David
"""

import pandas as pd
import numpy as np
import requests as requests
import json

weeks = list(range(17))
years = [2013, 2014, 2015, 2016]
finalList = []



def getWeekStats(base):
    for year in years:
        for week in weeks:
            data = requests.get(baseURL + "players/advanced?season=" + str(year) + "&week=" + str(week) + "&format=json&returnHTML=0")
            finalList.append(data.text)
    return finalList
    
    
    
baseURL = "http://api.fantasy.nfl.com/v1/"
test = getWeekStats(baseURL)

with open('outputFile.txt', 'w') as outfile:
    json.dump(test, outfile, ensure_ascii=False)    