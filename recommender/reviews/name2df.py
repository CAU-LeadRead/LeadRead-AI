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
review = pd.read_csv("reviews/reviews.csv")
name_col = review.columns[2::2]
for col in name_col:
    for name in review[col]:
        if type(name) == str and name.lower() not in names:
            names.append(name.lower())

for name in names:
    try:
        if "\\" in name:
            print(name)
            pass
    except:
        # print("error", name)
        pass
print(len(names))
print(names)
ids = list(range(len(names)))

d2 = {"perfumeId": ids, "title": names}
df2 = pd.DataFrame(data=d2)

print(df2.head())
df2.to_csv("recommender/ID_name.csv", index=False)