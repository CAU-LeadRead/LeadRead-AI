import mysql_reviews
from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds
import pandas as pd
import numpy as np
import sys
import json


def get_perfume_data():
    cursor = mysql_reviews.get_cursor()

    reviews_dict = mysql_reviews.get_reviews(cursor)

    user_perfume_data = pd.DataFrame(reviews_dict)

    user_perfume_data["title"] = (
        user_perfume_data["en_name"] + "/" + user_perfume_data["brand"]
    )

    user_perfume_data["rating"] = user_perfume_data["stars"].apply(pd.to_numeric)
    user_perfume_data["userId"] = user_perfume_data["UserNick"]
    nich = user_perfume_data[["title", "category"]]

    user_perfume_data.drop(
        [
            "id",
            "kr_brand",
            "kr_name",
            "longevity",
            "mood",
            "comment",
            "FragranceBrand",
            "brand",
            "en_name",
            "stars",
            "UserNick",
            "category",
        ],
        axis=1,
        inplace=True,
    )
    return user_perfume_data, nich


def get_corr():
    user_perfume_data, nich = get_perfume_data()
    user_perfume_rating = user_perfume_data.pivot_table(
        "rating", index="userId", columns="title"
    ).fillna(0)
    perfume_user_rating = user_perfume_rating.T
    SVD = TruncatedSVD(n_components=12)
    matrix = SVD.fit_transform(perfume_user_rating)
    corr = np.corrcoef(matrix)
    perfume_title = user_perfume_rating.columns
    return corr, perfume_title


def get_similar(perfume_name):
    user_perfume_data, nich = get_perfume_data()
    nich = nich.loc[nich["category"].isin([1])]["title"].values
    corr, perfume_title = get_corr()
    print(type(corr))
    perfume_title_list = list(perfume_title)
    corr_index = perfume_title_list.index(perfume_name)
    # print(perfume_title)
    result = list(perfume_title[(corr[corr_index] >= 0.7)])
    result2 = []
    for r in result:
        if r in nich:
            result2.append(r)
    return result2[:5]


def main():
    name = sys.argv[1]
    brand = sys.argv[2]
    perfume_name = name + "/" + brand
    similars = get_similar(perfume_name)
    result = []
    for sim in similars:
        result.append({"brand": sim.split("/")[1], "name": sim.split("/")[0]})
    result = json.dumps({"detected": result})
    print(result)


if __name__ == "__main__":
    main()
# print(get_similar("rose 31/le labo"))
"""
it's name
sorted by corr
"""
