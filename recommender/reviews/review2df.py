import numpy as np
import pandas as pd

"""
1. User ID | Product Name | Rating
2. Product Name | Product no.
------------------------------------
User ID | Product ID | Rating | Product Name
"""
# names from DB
names = open("names.txt", encoding="utf-8")
names = names.readlines()
names = [name.strip().lower() for name in names]

# names from survey
review = pd.read_csv("./reviews.csv")
name_col = review.columns[2::2]
for col in name_col:
    for name in review[col]:
        if type(name) == str and name.lower() not in names:
            names.append(name.lower())

df = pd.read_csv("reviews.csv")
ids = pd.read_csv("../ID_name.csv")
cols = df.columns[2:]
# print(len(cols))

data = []
usr = 0
for i in range(len(df[cols[0]].count)):
    review = df.iloc[i]
    for j in range(0, len(cols), 2):
        perfume = review[cols[j]]
        # print(perfume)
        if type(perfume) == str:
            perfume = perfume.lower()
            rating = review[cols[j + 1]]
            num = names.index(perfume)
            data.append([usr, num, rating, perfume])
    usr += 1

# print(data)

review = pd.DataFrame(data, columns=["userId", "perfumeId", "rating", "title"])

review.to_csv("recommender/user_review_jiho.csv", index=False)
