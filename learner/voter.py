from data_preprocessor import *
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier
import seaborn as sns; sns.set()

def voter(input_style):
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


    seed = 7
    kfold = model_selection.KFold(n_splits=10, random_state=seed)

    # create the sub models
    estimators = []
    model2 = RandomForestClassifier(n_estimators=1000)
    estimators.append(('rf', model2))
    model3 = SVC(gamma=0.01)
    estimators.append(('svm', model3))
    # create the ensemble model
    ensemble = VotingClassifier(estimators)
    results = model_selection.cross_val_score(ensemble, X, scores, cv=kfold)
    print(results.mean())






if __name__ == "__main__":
    voter(2)