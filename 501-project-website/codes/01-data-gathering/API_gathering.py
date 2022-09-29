import numpy as np
import requests
import csv
import json
import pandas as pd

url = "https://meteostat.p.rapidapi.com/stations/hourly"

querystring = {"station":"10637","start":"2020-01-01","end":"2020-01-01","tz":"Europe/Berlin"}

headers = {
	"X-RapidAPI-Key": "e120aadac9msh368877461acb279p1d91d1jsn1e95c3e7f715",
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.text
data_dict = json.loads(data)
df = pd.DataFrame.from_dict(data_dict['data'])
df.to_csv('501-project-website/data/datafile.csv', sep='\t')