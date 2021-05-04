import csv
import scipy.io
import csv
import pymysql
import os


base_dir = "./names_csv"
csvs = os.listdir(base_dir)

for csvfile in csvs:
    file_dir = os.path.join(base_dir, csvfile)
    f = open(file_dir, 'r')
    csvReader = csv.reader(f)
    name = [r[1] for r in csvReader]
    for n in name:
        c = name.count(n)
        if c != 1:
            print(n)
