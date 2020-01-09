from sklearn.svm import SVC
from data_preprocessor import *
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt


def svm(input_style):
    scores, behaviors, prefix = data_preprocessor(input_style)
    # print(behaviors[2])
    
    # n-gram of traj
    corpus = []
    for b in behaviors:
        corpus.append(' '.join(b))

    cv = CountVectorizer(ngram_range=(1, 4))
    cv_matrix = cv.fit_transform(corpus)
    cv_matrix = cv_matrix.toarray()
    vocab = cv.get_feature_names()
    # print(pd.DataFrame(cv_matrix, columns=vocab))

    # append the prefix to X
    for i in range(len(prefix)):
        if prefix[i]:
            prefix[i] = 0
        else:
            prefix[i] = 1
    X = np.column_stack((cv_matrix, prefix))
    vocab.append('prefix')

    # append the length to X
    traj_length = []
    for i in range(len(behaviors)):
        traj_length.append(len(behaviors[i]))
    X = np.column_stack((X, traj_length))
    vocab.append('traj_length')

    # append frequency of ready and ignore
    num_ready = []
    num_ignore = []
    for i in range(len(corpus)):
        num_ready.append(corpus[i].count('Ready'))
        num_ignore.append(corpus[i].count('Ignore'))
    X = np.column_stack((X, num_ready))
    vocab.append('num_ready')
    X = np.column_stack((X, num_ignore))
    vocab.append('num_ignore')




    print('length of vocab:', len(vocab))
    # print('list of vocab', vocab)

    # print(X[2])
    #todo: freq of ignore ready, back to back repetition, extract features
    # from interactoin (speech, motions)


    # # determines the number of components to choose for pca
    # pca = PCA().fit(X)
    # plt.plot(np.cumsum(pca.explained_variance_ratio_))
    # plt.xlabel('number of components')
    # plt.ylabel('cumulative explained variance')
    # plt.show()
    # # the number determined is 20

    # # plot to project data to 2 dimensions
    # pca = PCA(2)
    # projected = pca.fit_transform(X)
    # print(X.shape)
    # print(projected.shape)
    # plt.scatter(projected[:, 0], projected[:, 1],
    #             c=scores, edgecolor='none', alpha=0.5,
    #             cmap=plt.cm.get_cmap('Accent', 10))
    # plt.xlabel('component 1')
    # plt.ylabel('component 2')
    # plt.colorbar()
    # plt.show()


    # PCA and svm pipeline with grid search cross-validation for svm features
    n_components = 20
    pca = PCA(n_components=n_components, svd_solver='randomized',
              whiten=True).fit(X)

    X_train, X_test, y_train, y_test = train_test_split(X, scores,
                                                        test_size=0.20)
    svc = SVC(kernel='rbf')
    model = make_pipeline(pca, svc)
    param_grid = {'svc__C': [0.01, 0.1, 0.5, 1, 5, 10, 50, 60, 70, 80, 100, 1e3, 5e3],
                  'svc__gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01]}
    grid = GridSearchCV(model, param_grid, iid=True, cv=5)
    grid.fit(X_train, y_train)
    print("Best estimator found by grid search:")
    print(grid.best_params_)
    model = grid.best_estimator_
    y_pred = model.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))



if __name__ == "__main__":
    svm(2)