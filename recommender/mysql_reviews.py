import pymysql
import numpy as numpy
import pandas as pd


def get_cursor():
    db = pymysql.connect(
        user="admin",
        host="db-catchinichi.coagfxdx9ff4.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        password="Password!23",
        database="catchiNichi",
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
    stars=None,
):
    sql = "INSERT INTO reviews (brand, comment, en_name, kr_brand, kr_name, longevity, mood, userNick, stars) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
    sql = "INSERT INTO users (userNick, email) VALUES (%s, %s)"
    val = (userNick, email)
    cursor.execute(sql, val)
    db.commit()


def truncate(cursor):
    sql = "TRUNCATE reviews"
    cursor.execute(sql)
    db.commit()


if __name__ == "__main__":
    reviews = pd.read_csv("recommender/user_review_jiho.csv")
    # userId,name,brand,rating
    # truncate()
    values = []
    for index, row in reviews.iterrows():
        userNick = str(row["userId"])
        en_name = str(row["name"])
        brand = str(row["brand"])
        stars = str(row["rating"])
        v = [userNick, en_name, brand, stars]
        print(v)
        insert(userNick=v[0], en_name=v[1], brand=v[2], stars=v[3])
