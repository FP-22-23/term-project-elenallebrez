from collections import namedtuple

from datetime import datetime

import csv

maintuple=namedtuple("Student_number", "sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p,status,finish_date")

def read_dataset(file):
    with open (file, "r", encoding = "utf-8") as f:
        reader=csv.reader(f, delimiter = ";")
        next (reader)
        students=[maintuple(int(sl_no), gender, float(ssc_p), float(hsc_p), hsc_s, float(degree_p), degree_t, workex == "Yes",float(etest_p), specialisation, float(mba_p), status, datetime.strptime(finish_date, "%d/%m/%Y"))
        for sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex, etest_p,specialisation,mba_p,status,finish_date in reader]
    
    return students

#Second delivery

#First Block

#Function that filters and/or selects a series of rows and/or columns from the dataset
def hsc_p_filter(list, p=7500.0):
    filter=[]
    for e in list:
        if e.hsc_p >= p:
            filter.append(e)
    
    return filter


#Function that calculates the sum, total or average of a numerical property

def average_degree_percentage(list):
    i=0
    sum=0
    for e in list:
        sum=sum + e.degree_p
        i=i+1
    
    average= float(sum/i)

    return average, sum
    

#Second block

#A function that gets a tuple (or part of it) with the maximum or minimum value of a property from among tuples that meet a condition. 
def max_degree_p(list, year=2010):
    maximun=[]
    for e in list:
        if e.finish_date.year == year:
            maximun.append(e)
    
    max_tuple= max(maximun, key=lambda tup:tup[5])

    return max_tuple 


#Function that gets a list of n tuples ordered from major to minor (or minor to major) by a given property from among those that meet a condition
def order_mba_p_man(list, p=7500, m ="M"):
    filter=[]
    for e in list:
        if e.mba_p >= p and e.gender == m:
            filter.append(e)
    
    return sorted(filter)

def order_mba_p_woman(list, p=7500.0, f ="F"):
    filter=[]
    for e in list:
        if e.mba_p >= p and e.gender == f:
            filter.append(e)
    
    return sorted(filter)
