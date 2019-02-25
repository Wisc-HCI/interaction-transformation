from data_preprocessor import *
import numpy as np
import pandas as pd
from sklearn import cluster
# from sklearn import decomposition


def KMeans(input_style):

    scores, behaviors = data_preprocessor(input_style)

    categories = ['ReadyGreet', 'IgnoreGreet', 'ReadyHowHelp',
                  'IgnoreHowHelp',  'ReadyDidNotGetThat', 'IgnoreDidNotGetThat',
                  'ReadyCompleteQuery', 'IgnoreCompleteQuery', 'ReadyBye',
                  'IgnoreBye', 'ReadyAnswerQuery', 'IgnoreAnswerQuery',
                  'ReadyDidGet', 'IgnoreDidGet', 'ReadyInstruction1',
                  'IgnoreInstruction1', 'ReadyInstruction2"',
                  'IgnoreInstruction2"', 'ReadyWait', 'IgnoreWait',
                  'ReadyListOut', 'IgnoreListOut', 'ReadyAnecdote',
                  'IgnoreAnecdote', 'ReadyHowAreYou', 'IgnoreHowAreYou',
                  'ReadyNeedMoreHelp', 'IgnoreNeedMoreHelp']
    X = np.zeros((len(behaviors), len(categories)))

    # reshape the behaviors into (178,28) array where each entry represents
    # the number of occurrence of trajectory in one data entry.
    for i in range(len(X)):
        for j in range(len(X[i])):
            X[i][j] = behaviors[i].count(categories[j])

    # convert scores from -1, 0, 1 to 1, 2, 3
    for i in range(len(scores)):
        if scores[i] == -1:
            scores[i] = 1
        elif scores[i] == 0:
            scores[i] = 2
        else:
            scores[i] = 3
    X = np.column_stack((X, scores))
    categories.append('Scores')
    X_dataframe = pd.DataFrame(X, columns=categories)

    # to print out everything without omission
    # pd.set_option('display.max_columns', None)

    # print(X_dataframe.head(20))

    # to check if there is any missing data
    # print(X_dataframe.isna().head())

    n_clusters = 3
    k_means = cluster.KMeans(n_clusters=n_clusters)
    k_means.fit(X_dataframe)

    cluster_labels = k_means.labels_
    X_dataframe = X_dataframe.assign(cluster_labels=cluster_labels)
    grouped_X = X_dataframe.groupby('cluster_labels')
    for key, item in grouped_X:
        if key == 1:
            print(grouped_X.get_group(key), "\n")

if __name__ == "__main__":
    KMeans(1)


# # PCA example
# x1 = np.random.normal(size=100)
# x2 = np.random.normal(size=100)
# x3 = x1 + x2
# X = np.c_[x1, x2, x3]
#
# pca = decomposition.PCA()
# pca.fit(X)
# print(pca.explained_variance_)
#
# pca.n_components = 2
# X_reduced = pca.fit_transform(X)
# X_reduced.shape

