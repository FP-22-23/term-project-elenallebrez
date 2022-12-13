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

#Function that returns a dictionary that allows grouping by a property, in which values are a list or set with tuples that have the same value as that property.
def number_specialization(list):
    specialization=[]
    for e in list:
        specialization.append(e.hsc_s)
    
    return (Counter(specialization)) 

#Third Block
#Function that returns a maximum or minimum from a dictionary that corresponds to each key the sum of the values of a property of the tuples containing that key
def max_number_specialization(list):
    number = number_specialization(list)
    spec=max(number, key=number.get)
    
    return ("The specialization that more students chose is", max(number))

#Function that returns a dictionary that matches each key with the maximum or minimum of some property of the tuples containing that key.
def max_percentage(list):
    types=["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]
    
    percentage_ssc_p=max([e.ssc_p for e in list])
    percentage_hsc_p=max([e.hsc_p for e in list])
    percentage_degree_p=max([e.degree_p for e in list])
    percentage_etest_p=max([e.etest_p for e in list])
    percentage_mba_p=max([e.mba_p for e in list])
    percentage=[percentage_ssc_p, percentage_hsc_p, percentage_degree_p, percentage_etest_p, percentage_mba_p]

    total=dict(zip(types, percentage))


    return total


