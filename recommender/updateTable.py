import numpy as np
import pandas as pd
import mysql_reviews
import os

abs_path = os.path.dirname(os.path.realpath(__file__))


class MF:
    def __init__(self, R, K, alpha, beta, iterations):
        """
        Perform matrix factorization to predict empty
        entries in a matrix.

        Arguments
        - R (ndarray)   : user-item rating matrix
        - K (int)       : number of latent dimensions
        - alpha (float) : learning rate
        - beta (float)  : regularization parameter
        """

        self.R = R
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    def train(self):
        # Initialize user and item latent feature matrice
        self.P = np.random.normal(scale=1.0 / self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1.0 / self.K, size=(self.num_items, self.K))

        # Initialize the biases
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.R[np.where(self.R != 0)])

        # Create a list of training samples
        self.samples = [
            (i, j, self.R[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.R[i, j] > 0
        ]

        # Perform stochastic gradient descent for number of iterations
        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))
            if (i + 1) % 10 == 0:
                print("Iteration: %d ; error = %.4f" % (i + 1, mse))

        return training_process

    def mse(self):
        """
        A function to compute the total mean square error
        """
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x, y in zip(xs, ys):
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return np.sqrt(error)

    def sgd(self):
        """
        Perform stochastic graident descent
        """
        for i, j, r in self.samples:
            # Computer prediction and error
            prediction = self.get_rating(i, j)
            e = r - prediction

            # Update biases
            self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])

            # Update user and item latent feature matrices
            self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i, :])
            self.Q[j, :] += self.alpha * (e * self.P[i, :] - self.beta * self.Q[j, :])

    def get_rating(self, i, j):
        """
        Get the predicted rating of user i and item j
        """
        prediction = (
            self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        )
        return prediction

    def full_matrix(self):
        """
        Computer the full matrix using the resultant biases, P and Q
        """
        return (
            self.b
            + self.b_u[:, np.newaxis]
            + self.b_i[
                np.newaxis :,
            ]
            + self.P.dot(self.Q.T)
        )


def get_user_perfume_data():
    cursor = mysql_reviews.get_cursor()

    reviews_dict = mysql_reviews.get_reviews(cursor)

    user_perfume_data = pd.DataFrame(reviews_dict)

    user_perfume_data["title"] = (
        user_perfume_data["en_name"] + "/" + user_perfume_data["brand"]
    )

    user_perfume_data["rating"] = user_perfume_data["stars"].apply(pd.to_numeric)
    user_perfume_data["userId"] = user_perfume_data["UserNick"]
    nich = user_perfume_data[["userId", "title", "category"]]

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


def get_perfume_matrix():
    user_perfume_data, nich = get_user_perfume_data()
    df_user_perfume_rating = user_perfume_data.pivot_table(
        "rating", index="userId", columns="title"
    ).fillna(0)
    user_list = df_user_perfume_rating.index.values
    user_row_dict = dict(zip(list(user_list), range(len(user_list))))
    matrix = df_user_perfume_rating.values
    return matrix, user_row_dict, df_user_perfume_rating


def predict(k=20, a=0.03, b=0.001, iter=1000):
    matrix, user_row_dict, df_user_perfume_rating = get_perfume_matrix()
    mf = MF(matrix, K=k, alpha=a, beta=b, iterations=iter)
    mf.train()
    prediction = mf.full_matrix()
    df_preds = pd.DataFrame(prediction, columns=df_user_perfume_rating.columns)
    return df_preds, user_row_dict, df_preds


def recommend_perfumes(
    user_id, df_preds, user_row_dict, df_user_perfume_rating, num_recommendations=5
):
    # df_preds, user_row_dict, df_user_perfume_rating = predict(iter=1000)
    user_perfume_data, nich = get_user_perfume_data()
    user_row_number = user_row_dict[user_id]
    sorted_user_predictions = df_preds.iloc[user_row_number].sort_values(
        ascending=False
    )
    user_history = user_perfume_data[user_perfume_data.userId == user_id].sort_values(
        ["rating"], ascending=False
    )
    user_perfume_data = user_perfume_data.loc[nich["category"].isin([1])]
    recommendations = user_perfume_data[
        ~user_perfume_data["title"].isin(user_history["title"])
    ]
    recommendations = recommendations.merge(
        pd.DataFrame(sorted_user_predictions).reset_index(), on="title"
    )
    recommendations = recommendations.rename(
        columns={user_row_number: "Predictions"}
    ).sort_values("Predictions", ascending=False)
    recommendations.reset_index(inplace=True)
    recommendations.drop(["userId", "rating", "index"], axis=1, inplace=True)
    recommendations.drop_duplicates(inplace=True)
    recommendations = recommendations.iloc[:num_recommendations, :]
    return recommendations, user_history


def main():
    df_preds, user_row_dict, df_user_perfume_rating = predict(k=14, iter=500)
    df_preds.to_csv(
        os.path.join(abs_path, "DataFrames/df_preds.csv"), index_label="title"
    )
    user_row_df = pd.DataFrame.from_dict(user_row_dict, orient="index")
    user_row_df.to_csv(os.path.join(abs_path, "DataFrames/user_row_df.csv"))


if __name__ == "__main__":
    main()