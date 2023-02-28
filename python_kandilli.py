import json
import psycopg2 as psyc
import requests
from bs4 import BeautifulSoup
import pandas as pd
connection = psyc.connect(
    database = "postgres",
    user = "postgres",
    password = "123456",
    host = "127.0.0.1",
    port = "5432"
)
connection.autocommit = True
#deprem2 = "CREATE DATABASE deprem2"
cursor = connection.cursor()
#cursor.execute(deprem2)

database = "deprem2"

connection2 = psyc.connect(
    database = database,
    user = "postgres",
    password = "123456",
    host = "127.0.0.1",
    port = "5432"
)
# veri çekme işlemi
headers = {
    'authority': 'api.berkealp.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
response = requests.get("https://api.berkealp.net/kandilli/index.php?all", headers=headers)
#create_table_deprem2 =
"""
CREATE TABLE deprem2(
id VARCHAR(100) PRIMARY KEY,
tarih DATE,
EnlemN VARCHAR(50),
BoylamE VARCHAR(50),
DerinlikKM VARCHAR(50),
ML FLOAT,
Yer VARCHAR(255))"""
connection2.autocommit = True
cursor = connection2.cursor()
#cursor.execute(create_table_deprem2)

for i in response.json():
    #print(i)
   # print("Time", "Magnitude", "Latitude", "Longitude", "Depth", "Region")
    veri2 = (i["ID"], i["Time"], i["Magnitude"], i["Latitude"].replace("&deg; N", ""), i["Longitude"].replace("&deg; E", ""), i["Depth"], i["Region"])
    veri3 = []

    veri3.append(veri2)
    print(veri3)
    veri3_record = ", ".join(["%s"] * len(veri3))
    query_insert = (
        f"INSERT INTO deprem2(id, tarih, ML, EnlemN, BoylamE, DerinlikKM, Yer) values {veri3_record}"

    )
    connection2.autocommit = True
    count = cursor.rowcount
    #cursor.execute(query_insert, veri3)

print(count)










