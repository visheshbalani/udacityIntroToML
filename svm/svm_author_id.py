#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(kernel = 'linear')
"""
for i in range(7):
	cval = 10**i
	print 'Value of c is ', cval
	clf = SVC(kernel = 'rbf', C = cval )
	t0 = time()
	clf.fit(features_train, labels_train)
	print 'training time', time() - t0, 'seconds'

	t1 = time()
	clf.predict(features_test)  #pred
	print 'predicition time', time() - t1, 'seconds'

	accuracy = clf.score(features_test, labels_test)
	print accuracy
"""
clf = SVC(kernel = 'rbf', C = 10000 )
t0 = time()
clf.fit(features_train, labels_train)
print 'training time', time() - t0, 'seconds'

t1 = time()
pred = clf.predict(features_test)  #pred
print 'predicition time', time() - t1, 'seconds'

accuracy = clf.score(features_test, labels_test)
print accuracy

"""
from sklearn.metrics import classification_report
target_names = ['0 Sara','1 Chris']
print(classification_report(labels_test, target_names = target_names))
"""

count = 0
for i in range(len(pred)):
	if(pred[i] == 1):
		count+=1
print '1 Chris: ', count


#print pred[10]
#print pred[26]
#print pred[50]
#from sklearn.metrics import accuracy_score
#accuracy_score(pred, labels_test)
#########################################################


