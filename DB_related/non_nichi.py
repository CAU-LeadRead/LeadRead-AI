import pymysql
import numpy as numpy
import pandas as pd
import requests
import time

db = pymysql.connect(
    user="admin",
    host="db-catchinichi.coagfxdx9ff4.ap-northeast-2.rds.amazonaws.com",
    port=3306,
    password="Password!23",
    database="catchiNichi",
    charset="utf8",
)
cursor = db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM reviews"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result)
result = result[result["category"] == 0]

df = result[["en_name", "brand"]].drop_duplicates()
# print(df.head())


def insert(en_name, brand, category=0):
    sql = "INSERT INTO fragrances (brand, en_name, category) VALUES(%s, %s, %s)"
    val = (brand, en_name, category)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.lastrowid)


def delete():
    sql = "DELETE FROM fragrances WHERE category = 0"
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount)


# delete()

nichi = [
    "byredo",
    "creed",
    "acquadiparma",
    "diptyque",
    "jomalone",
    "maisonmargiela",
    "santamarianovella",
]

for index, row in df.iterrows():
    if row["brand"] not in nichi:
        insert(row["en_name"], row["brand"])
    # print(row["en_name"],row["brand"])

nafla = [
    "strawberry",
    "orange",
    "lemon",
    "rose",
    "jasmine",
    "pine tree",
    "ocean",
    "forest",
    "pepper",
    "bakery",
]

for n in nafla:
    insert(n, "natural", category=2)


# print(result.head())
