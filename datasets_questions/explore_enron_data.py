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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'Feature count:', len(enron_data.values()[0])

poi_count = len([p for p, f in enron_data.iteritems() if 1 == f['poi']])
print 'POI count:', poi_count

print 'James Prentice Stock Value:', enron_data['PRENTICE JAMES']['total_stock_value']

print 'Email from Wesley Colwell:', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'Stock options exercised by Jeffrey K Skilling:', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

for p in [ 'LAY KENNETH L', 'SKILLING JEFFREY K', 'FASTOW ANDREW S' ]:
  print 'Total payments for ', p, ':', enron_data[p]['total_payments']

print 'Folks with quantified salary:', len([f['salary'] for f in enron_data.values() if 'NaN' != f['salary']])

print 'Folks with a known email address', len([f['email_address'] for f in enron_data.values() if 'NaN' != f['email_address']])

no_total_payment = 1.0 * len([f['total_payments'] for f in enron_data.values() if 'NaN' == f['total_payments']])
print 'People with no total payment:', no_total_payment, no_total_payment / len(enron_data) * 100

poi_no_total_payment = 1.0 * len([f['total_payments'] for f in enron_data.values() if 'NaN' == f['total_payments'] and 1 == f['poi']])
print 'POI\'s with no total payment:', poi_no_total_payment, poi_no_total_payment / poi_count * 100
