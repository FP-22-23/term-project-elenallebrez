from collections import namedtuple, defaultdict, Counter

from datetime import datetime

import csv

maintuple=namedtuple("Student_number", "sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p,status,finish_date")

#FIRST DELIVERY

def read_dataset(file):
    with open (file, "r", encoding = "utf-8") as f:
        reader=csv.reader(f, delimiter = ";")
        next (reader)
        students=[maintuple(int(sl_no), gender, float(ssc_p)/100, float(hsc_p)/100, hsc_s, float(degree_p)/100, degree_t, workex == "Yes",float(etest_p)/100, specialisation, float(mba_p)/100, status, datetime.strptime(finish_date, "%d/%m/%Y"))
        for sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex, etest_p,specialisation,mba_p,status,finish_date in reader]
    
    return students

#SECOND DELIVERY

#BLOCK 1
#Función que filtre y/o seleccione una serie de filas y/o columnas del dataset
def preuniversity_p_filter(mylist, p=75.00):
    filter=[e for e in mylist if e.hsc_p >= p and e.ssc_p >= p]
    return ("The total number of students whose preuniversity percentages are higher that 75.0 are: ", len(filter), ". These are the first 10s: ", filter[:10])

def working_students(mylist):
    filter=[e for e in mylist if e.workex == True and e.status == "Placed"]
    return ("These are the students who has working experience and are now working", filter)

#Función que cuente el número de valores distintos de un atributo, o que devuelva un conjunto con los valores distintos
def diferent_specialization(mylist):
    high_school = [e.hsc_s for e in mylist]
    degree=[e.degree_t for e in mylist]
    specialisation_master=[e.specialisation for e in mylist]

    high_school1= set(high_school)
    degree1= set(degree)
    specialisation_master1=set(specialisation_master)
    
    return ("In high school students could chose one of this options: ", high_school1, ". At university, these were the options: ", degree1, ". And the mba specializations were: ", specialisation_master1)

#Función que calcule la suma, el total o la media de una propiedad numérica
def average_degree_percentage(mylist):
    i=0
    sum=0
    for e in mylist:
        sum=sum + e.degree_p
        i=i+1
    
    average= float(sum/i)

    return("The total sum of the degree percentages is: ", sum, ", the total number of students is: ", len(mylist), " so the average of all the degree precentages is: ", average)


#BLOCK 2
#Función que obtenga una tupla (o una parte de ella) con el valor máximo o mínimo de una propiedad
#de entre las tuplas que cumplan una condición. 
def max_degree_p_year(mylist):
    year_2010 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2010)
    year_2011 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2011)
    year_2012 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2012)
    year_2013 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2013)
    year_2014 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2014)
    year_2015 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2015)
    year_2016 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2016)
    year_2017 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2017)
    year_2018 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2018)
    year_2019 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == 2019)

    
    return ("The student that has the maximun degree percentage in 2010 is: ", year_2010,
    "The student that has the maximun degree percentage in 2011 is: ", year_2011,
    "The student that has the maximun degree percentage in 2012 is: ", year_2012,
    "The student that has the maximun degree percentage in 2013 is: ", year_2013,
    "The student that has the maximun degree percentage in 2014 is: ", year_2014, 
    "The student that has the maximun degree percentage in 2015 is: ", year_2015,
    "The student that has the maximun degree percentage in 2016 is: ", year_2016,
    "The student that has the maximun degree percentage in 2017 is: ", year_2017,
    "The student that has the maximun degree percentage in 2018 is: ", year_2018,
    "The student that has the maximun degree percentage in 2019 is: ", year_2019)

#Función que obtenga una lista con las tuplas cuyo valor de una propiedad concreta es igual al
#máximo o mínimo valor de esa propiedad
def max_degree_p(mylist):
    higher_degree_p = max([e.degree_p for e in mylist])
    student_higher = [e for e in mylist if e.degree_p == higher_degree_p]

    lower_degree_p = min([e.degree_p for e in mylist])
    student_lower = [e for e in mylist if e.degree_p == lower_degree_p]

    return ("The student with the maximun degree percentage is: ", student_higher, " and the lowest is: ", student_lower)


#Función que obtenga una lista con n tuplas ordenadas de mayor a menor (o de menor a mayor) por 
#una propiedad determinada de entre las que cumplan una condición
def order_mba_p_man(mylist, p=65.0, m ="M", n = 3):
    filter=[e for e in mylist if e.mba_p >= p and e.gender == m][:n]
    order= sorted(filter, key = lambda x:x[-3], reverse= True)
    
    return ("The men whose master percentage is higher than 75.0 are: ", order)

def order_mba_p_woman(mylist, p=65.0, f ="F", n=3):
    filter=[e for e in mylist if e.mba_p >= p and e.gender == f][:n]
    order= sorted(filter, key = lambda x:x[-3] ,reverse= True)
    return ("The women whose master percentage is higher than 75.0 are: ", order)

#Función que devuelva un diccionario que permita agrupar por una propiedad, en el que los valores 
#sean una lista o un conjunto con las tuplas que tienen el mismo valor de esa propiedad.

def group_hsc_s(mylist):
    d=dict()
    specialization={"Arts", "Commerce", "Science"}
    for e in specialization:
        total_list=[i.sl_no for i in mylist if e == i.hsc_s]
        d[e]= total_list
    
    return d

#THIRD DELIVERY

#BLOCK 3
#EJERCICIO 8
def number_hsc_s(mylist):
    specialization=[e.hsc_s for e in mylist]
    count=Counter(specialization)
    return count

def number_degree_t(mylist):
    specialization=[e.degree_t for e in mylist]
    count=Counter(specialization)
    return count

def number_specialization(mylist):
    specialization=[e.specialisation for e in mylist]
    count=Counter(specialization)
    return count

#EJERCICIO 11

def max_number_hsc_s(mylist):
    number = number_hsc_s(mylist)
    spec=max(number, key=number.get)
    return ("The specialization in high school that more students chose is", spec)

def max_number_degree_t(mylist):
    number = number_degree_t(mylist)
    spec=max(number, key=number.get)
    return ("The type of degree that more students chose is", spec)

def max_number_specialization(mylist):
    number = number_specialization(mylist)
    spec=max(number, key=number.get)
    return ("The specialization that more students chose is", spec)

#Función que devuelva un diccionario que hace corresponder a cada clave el máximo o mínimo de 
#alguna propiedad de las tuplas que contienen dicha clave.

def max_percentage(mylist):
    types=["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]
    
    percentage_ssc_p=max([e.ssc_p for e in mylist])
    percentage_hsc_p=max([e.hsc_p for e in mylist])
    percentage_degree_p=max([e.degree_p for e in mylist])
    percentage_etest_p=max([e.etest_p for e in mylist])
    percentage_mba_p=max([e.mba_p for e in mylist])
    percentage=[percentage_ssc_p, percentage_hsc_p, percentage_degree_p, percentage_etest_p, percentage_mba_p]

    total=dict(zip(types, percentage))


    return ("The maximun percentages in each test or course are: ", total) 

#Función que devuelva un diccionario que hace corresponder a cada clave una lista ordenada con los 
#n mayores o menores elementos que contienen dicha clave

def top5_percentage_working(mylist, n = 5):
    types=["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]
    
    percentage_ssc_p=sorted([e.ssc_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_hsc_p=sorted([e.hsc_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_degree_p=sorted([e.degree_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_etest_p=sorted([e.etest_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_mba_p=sorted([e.mba_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage=[percentage_ssc_p, percentage_hsc_p, percentage_degree_p, percentage_etest_p, percentage_mba_p]
    
    total=dict(zip(types, percentage))
    return ("This are the top 5 scores of all tests of the students that have working experience ",total)

#Función que devuelva un diccionario que hace corresponder a cada clave el porcentaje de alguna
#propiedad de las tuplas que contienen dicha clave respecto al total de tuplas

def porcentage_working(mylist):
    working = [e.status for e in mylist if e.status == "Placed"]
    percentage = (len(working)*100)/len(mylist)

    return percentage

def percentage_A(mylist):
    A = [e for e in mylist if e.ssc_p >= 75 and e.hsc_p >= 75 and e.degree_p >= 75 and e.etest_p >= 75 and e.mba_p >= 75]
    percentage = (len(A)*100)/len(mylist)

    return percentage
