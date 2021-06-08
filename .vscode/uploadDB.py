import scipy.io
import csv
import pymysql
import os

conn = pymysql.connect(host='db-catchinichi.coagfxdx9ff4.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin',
                       password='Password!23', db='catchiNichi', charset='utf8')

curs = conn.cursor()
conn.commit()

base_dir = "./names_csv"
csvs = os.listdir(base_dir)

for csvfile in csvs:
    file_dir = os.path.join(base_dir, csvfile)
    f = open(file_dir, 'r')
    csvReader = csv.reader(f)

    for row in csvReader:

        brand = (row[0])

        en_name = (row[1])

        print(brand)

        print(en_name)

        sql = """insert into `fragrances` (`brand`, `en_name`) values (%s, %s)"""

        curs.execute(sql, (brand, en_name))

    # db의 변화 저장

    conn.commit()

    f.close()

conn.close()
