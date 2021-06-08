import numpy as np
import pandas as pd

"""
1. User ID | Product Name | Rating
2. Product Name | Product no.
------------------------------------
User ID | Product ID | Rating | Product Name
"""

df = pd.read_csv("recommender/reviews/reviews.csv")
cols = df.columns[2:]
# print(len(cols))

print(df[cols[0]].count())

data = []
usr = 0
for i in range(df[cols[0]].count()):
    review = df.iloc[i]
    for j in range(0, len(cols), 2):
        perfume = review[cols[j]]
        # print(perfume)
        if type(perfume) == str:
            perfume = perfume.lower()
            rating = review[cols[j + 1]]
            data.append([usr, perfume, rating])
    usr += 1

# print(data)

review = pd.DataFrame(data, columns=["userId", "title", "rating"])

review.to_csv("recommender/user_review_jiho.csv", index=False)
