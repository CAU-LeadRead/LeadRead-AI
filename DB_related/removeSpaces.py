import pymysql
import pandas as pd

fragrance = pd.read_csv("fragrancelist.csv")
fragrance["brand"] = fragrance["brand"].apply(str.strip).apply(str.lower)
fragrance["en_name"] = fragrance["en_name"].apply(str.strip).apply(str.lower)
fragrance.to_csv("aaa.csv")