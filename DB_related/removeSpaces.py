import pymysql
import pandas as pd

fragrance = pd.read_csv("DB_related/fragrance.csv")
fragrance["brand"] = fragrance["brand"].str.replace(" ", "")
fragrance["en_name"] = fragrance["en_name"].str.replace(" ", "")
fragrance.to_csv("DB_related/temp.csv")