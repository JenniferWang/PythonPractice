import pickle
import numpy as np
#import sklearn
import random
# import numpy as np
import time
from sklearn import linear_model
from sklearn import cross_validation


seed_ = np.random.choice(range(100))
np.random.seed(int(time.time()))

data_pkl_file = open('data.pkl', 'rb')
data = pickle.load(data_pkl_file)
target_pkl_file = open('target.pkl', 'rb')
targets = pickle.load(target_pkl_file)

d_t = list(zip(data, targets))
random.shuffle(d_t)

data = [d_t_[0] for d_t_ in d_t]
targets = [d_t_[1] for d_t_ in d_t]

data_test_pkl_file = open('data_test.pkl', 'rb')
data_test = pickle.load(data_test_pkl_file)
target_test_pkl_file = open('target_test.pkl', 'rb')
targets_test = pickle.load(target_test_pkl_file)

data.extend(data_test)
targets.extend(targets_test)

#data_test = np.array(data_test)
#targets_test = np.array(targets_test).reshape(len(targets_test))

data = np.array(data)
targets = np.array(targets).reshape(len(targets))

#X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, targets, test_size=0.2,random_state=None)
clf = linear_model.LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=0.01, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=seed_)
scores = cross_validation.cross_val_score(clf, data, targets, cv=5)
print(scores)


#clf.fit(data, targets)
#print(clf.score(data_test, targets_test)) 
