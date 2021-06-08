import pymysql
import numpy as numpy
import pandas as pd
import requests
import time

db = pymysql.connect(
    user="username",
    host="host url",
    port=3306,
    password="password",
    database="database",
    charset="utf8",
)
cursor = db.cursor(pymysql.cursors.DictCursor)


def get_cursor():
    db = pymysql.connect(
        user="username",
        host="host url",
        port=3306,
        password="password",
        database="database",
        charset="utf8",
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return cursor


def insert(
    cursor,
    brand=None,
    comment=None,
    en_name=None,
    kr_brand=None,
    kr_name=None,
    longevity=None,
    mood=None,
    userNick=None,
    category=0,
    stars=None,
):
    sql = "INSERT INTO reviews (brand, comment, en_name, kr_brand, kr_name, longevity, mood, userNick, stars, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (brand, comment, en_name, kr_brand, kr_name, longevity, mood, userNick, stars)
    cursor.execute(sql, val)
    db.commit()
    print("inserted row ID: ", cursor.lastrowid)


def delete(cursor, name):
    sql = "DELETE FROM reviews WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    db.commit()
    print(cursor.rowcount, "record(s) deleted")


def get_reviews(cursor):
    sql = "SELECT * FROM reviews"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def addUser(cursor, userNick, email):
    sql = "INSERT INTO users (nick, email) VALUES (%s, %s)"
    val = (userNick, email)
    cursor.execute(sql, val)
    db.commit()


def truncate(cursor):
    sql = "TRUNCATE reviews"
    cursor.execute(sql)
    db.commit()


def upload_data(
    brand=None,
    comment=None,
    en_name=None,
    kr_brand=None,
    kr_name=None,
    longevity=None,
    mood=None,
    userNick=None,
    category=0,
    stars=None,
):
    nichi_list = [
        "diptyque",
        "jomalone",
        "santa maria novella",
        "byredo",
        "acqua di parma",
        "creed",
        "masion margiella",
    ]
    if brand in nichi_list:
        category = 1
    url = "https://ziho-dev.com/review/addReview"
    obj = {
        "brand": brand,
        "comment": comment,
        "en_name": en_name,
        "longevity": longevity,
        "mood": mood,
        "nick": userNick,
        "category": category,
        "stars": stars,
    }
    r = requests.post(url, obj)
    print(r)


if __name__ == "__main__":
    print(get_reviews(cursor))
    # truncate(cursor)
    # print("hi")

    # for i in range(40):
    #     nick = "a" + str(i)
    #     email = nick + "@gmail.com"
    #     addUser(cursor, nick, email)

    reviews = pd.read_csv("recommender/user_review_jiho.csv")
    for index, row in reviews.iterrows():
        userNick = str(row["userId"])
        en_name = str(row["name"]).lower().replace(" ", "").strip()
        brand = str(row["brand"]).lower().replace(" ", "").strip()
        stars = int(row["rating"])
        upload_data(en_name=en_name, userNick=userNick, brand=str(brand), stars=stars)
        # print(en_name, brand, stars)
        # time.sleep(0.5)
        # v = [userNick, en_name, brand, stars]
        # print(v)
    #     insert(cursor, userNick="a" + v[0], en_name=v[1], brand=v[2], stars=v[3])
    df = pd.DataFrame(get_reviews(cursor))
    print(df.head(10))
