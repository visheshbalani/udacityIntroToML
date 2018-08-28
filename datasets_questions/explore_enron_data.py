#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
import json
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
number_of_people = len(enron_data)
print number_of_people
print enron_data["SKILLING JEFFREY K"]
print len(enron_data["SKILLING JEFFREY K"])

#df = pd.DataFrame(list(enron_data.items()))
#print df.head()
#print df.describe()

#print "people"
#for k in enron_data:
#	print k

print "Jeff",  enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "James Prentice stock: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

cnt = 0
for k,v in enron_data.iteritems():
	if(enron_data[k]["poi"] == 1):
		cnt+=1
print "poi", cnt

print "Lay, Chairman", enron_data["LAY KENNETH L"]["total_payments"] 
print "Skilling, CEO", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Fastow, CFO", enron_data["FASTOW ANDREW S"]["total_payments"]

salarycnt = 0
for k,v in enron_data.iteritems():
	if(enron_data[k]["salary"]=="NaN"):
		salarycnt +=1
print number_of_people - salarycnt
#Fkn do !="NaN"
emailcnt = 0
for k, v in enron_data.iteritems():
	if(enron_data[k]["email_address"]=="NaN"):
		emailcnt +=1

print number_of_people - emailcnt	

emptypay = 0
for k, v in enron_data.iteritems():
        if(enron_data[k]["total_payments"]=="NaN"):
                emptypay +=1
print emptypay
print float(emptypay)/number_of_people

emptypaypoi = 0
for k, v in enron_data.iteritems():
        if(enron_data[k]["total_payments"]=="NaN" and enron_data[k]["poi"] == 1):
                emptypaypoi +=1
print emptypaypoi
print float(emptypaypoi)/number_of_people
