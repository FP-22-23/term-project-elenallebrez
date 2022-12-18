from collections import namedtuple, defaultdict, Counter

from datetime import datetime

import csv

maintuple=namedtuple("Student_number", "sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p,status,finish_date")

#FIRST DELIVERY
    '''
    Returns a list of tuples of type Student_number based on the data included in the file csv given as a parameter. This data set is encoding in utf-8
    @param fichero:Name and path of the csv file to read.
    @type fichero:srt
    @return: list of tuples of type Student_number based on the data
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    '''
def read_dataset(file):
    with open (file, "r", encoding = "utf-8") as f:
        reader=csv.reader(f, delimiter = ";")
        next (reader)
        students=[maintuple(int(sl_no), gender, float(ssc_p)/100, float(hsc_p)/100, hsc_s, float(degree_p)/100, degree_t, workex == "Yes",float(etest_p)/100, specialisation, float(mba_p)/100, status, datetime.strptime(finish_date, "%d/%m/%Y"))
        for sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex, etest_p,specialisation,mba_p,status,finish_date in reader]
    
    return students

# SECOND DELIVERY

# Block 1

def preuniversity_p_filter(mylist, p=75.00):
    '''
    It returns a list of tuples of type Student_number with the data of the people who have passed high school and high school with a percentage greater than p
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param p: number by which the students will be filtered. It can take any value you want, from 0 to 100. If p is not specified take 75. 00 as default value
    @type p: int
    @return: List of tuples of type Student_number with the students that meet the conditions.
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]] 
    '''
    filter=[e for e in mylist if e.hsc_p >= p and e.ssc_p >= p]
    return filter

def working_students(mylist, work = True, now = "Placed"):
'''
    Returns a list of tuples of type Student_number with the data of the people who have working experience and are now working
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param work: is True when workex = "Yes", so it represents the work experience
    @type work: boolean
    @param now: character string which can be "Placed" or "Not Placed" depending if the student is working or not. If this value is not specified, it will take "Placed" as default value
    @type now: str
    @return: List of tuples of type Student_number with the students that meet the conditions.
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]] 
    '''
    filter=[e for e in mylist if e.workex == work and e.status == now]
    return  filter

def diferent_specialization(mylist):
    '''
    It returns three different sets, each set being the choices students have had throughout their lives. The first set are the specialization options at the institute,
    the second, the undergraduate options, and the last set the master's specialization options.
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: set made of three elements of str type
    @rtype: set()
    '''
    
    high_school = [e.hsc_s for e in mylist]
    degree=[e.degree_t for e in mylist]
    specialisation_master=[e.specialisation for e in mylist]

    high_school1= set(high_school)
    degree1= set(degree)
    specialisation_master1=set(specialisation_master)
    
    return high_school1, degree1, specialisation_master1

def average_degree_percentage(mylist):
    '''
    This function calculates and returns the sum, the number of students and the average degree's percentage
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: the total sum, number of students and the average of the percentage
    @rtype: float, int, float
    '''
    i=0
    sum=0
    for e in mylist:
        sum=sum + e.degree_p
        i=i+1
    
    average= float(sum/i)

    return  sum, i, average

# Block 2

def max_degree_p_2010(mylist, year = 2010):
    '''
    Returns a tuple with the maximum percentage obtained by a student in the degree during the year 2010. This tuple contains the student's serial number and the percentage obtained.
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param year: This number is the year I have chosen to see what was the best grade that year. It can be changed, but the default value is 2010.
    @type year: int
    @return: tuple with the serial number of the student and the degree percentage
    @rtype: tuple()
    '''
    year_2010 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == year)
    
    return  year_2010

def max_degree_p_2019(mylist, year = 2019):
    '''
    Returns a tuple with the maximum percentage obtained by a student in the degree during the year 2019. This tuple contains the student's serial number and the percentage obtained.
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param year: This number is the year I have chosen to see what was the best grade that year. It can be changed, but the default value is 2019.
    @type year: int
    @return: tuple with the serial number of the student and the degree percentage
    @rtype: tuple()
    '''
    year_2019 = max((e.sl_no, e.degree_p) for e in mylist if e.finish_date.year == year)
    
    return  year_2019

def max_min_degree_p(mylist):
    '''
    Returns two list of tuples of type Student_number, the first one is the students with the highest degree percentage and the second is the students with the lowest degree percentage
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: List of tuples of type Student_number with the students that meet the conditions.
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    '''
    higher_degree_p = max([e.degree_p for e in mylist])
    student_higher = [e for e in mylist if e.degree_p == higher_degree_p]

    lower_degree_p = min([e.degree_p for e in mylist])
    student_lower = [e for e in mylist if e.degree_p == lower_degree_p]

    return  student_higher, student_lower

def order_mba_p_man(mylist, p=65.0, m ="M", n = 3):
    '''
    Returns a list with 3 tuples of type Student_number that represent the top 3 male students with a master percentage higher than 65.0
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param n: number by which the male students will be filtered. It can take any value you want. If n is not specified, it will take 65.00 as default value
    @type n: int
    @param m: character string which represents the gender, it can be "M" or "F". If m is not specified, it will take "M" as default value
    @type m: str
    @return: List of tuples of type Student_number with the students that meet the conditions.
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    '''
    filter=[e for e in mylist if e.mba_p >= p and e.gender == m][:n]
    order= sorted(filter, key = lambda x:x[-3], reverse= True)
    
    return order

def order_mba_p_woman(mylist, p=65.0, f ="F", n=3):
    '''
    It returns a list with 3 tuples of type Student_number that represent the top 3 female students with a master percentage higher than 65.0
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param n: number by which the female students will be filtered. It can take any value you want. If n is not specified, it will take 65.00 as default value
    @type n: int
    @param f: character string which represents the gender, it can be "M" or "F". If m is not specified, it will take "F" as default value
    @type f: str
    @return: List of tuples of type Student_number with the students that meet the conditions.
    @rtype: [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    '''
    filter=[e for e in mylist if e.mba_p >= p and e.gender == f][:n]
    order= sorted(filter, key = lambda x:x[-3] ,reverse= True)
    return order

def group_hsc_s(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns a dictionary whose keys are the types of specializations of high school and the value is a list with the serial number 
    of the students who chose that specialization.
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: a dictionary whose keys are the types of specializations of high school and the value is a list with the serial number of the students who chose that specialization.
    @rtype: {str: int}
    '''
    
    d=dict()
    specialization={"Arts", "Commerce", "Science"}
    for e in specialization:
        total_list=[i.sl_no for i in mylist if e == i.hsc_s]
        d[e]= total_list
    
    return d

# THIRD DELIVERY

# Block 3

def number_hsc_s(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns a dictionary whose keys are the types of specializations of high school and the value is the number of students that chose that specialization
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: a dictionary whose keys are the types of specializations of high school and the value is the number of students that chose that specialization
    @rtype: {str: int}
    '''
    specialization=[e.hsc_s for e in mylist]
    count=Counter(specialization)
    return count

def number_degree_t(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns a dictionary whose keys are the types of specializations of degree and the value is the number of students that chose that specialization
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: a dictionary whose keys are the types of specializations of degree and the value is the number of students that chose that specialization
    @rtype: {str: int}
    '''
    specialization=[e.degree_t for e in mylist]
    count=Counter(specialization)
    return count

def number_specialization(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns a dictionary whose keys are the types of specializations of the master and the value is the number of students that chose that specialization
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: a dictionary whose keys are the types of specializations of the master and the value is the number of students that chose that specialization
    @rtype: {str: int}
    '''
    specialization=[e.specialisation for e in mylist]
    count=Counter(specialization)
    return count

def max_number_hsc_s(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns the specialization of the high school where there is more students
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: the specialization of the high school where there is more students
    @rtype: str
    '''
    number = number_hsc_s(mylist)
    spec=max(number, key=number.get)
    return spec

def max_number_degree_t(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns the specialization of the degree where there is more students
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: the specialization of the degree where there is more students
    @rtype: str
    '''
    number = number_degree_t(mylist)
    spec=max(number, key=number.get)
    return  spec

def max_number_specialization(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns the specialization of the master where there is more students
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: the specialization of the master where there is more students
    @rtype: str
    '''
    number = number_specialization(mylist)
    spec=max(number, key=number.get)
    return  spec

def max_percentage(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns a dictionary whose keys are the types tests and the value is the maximun percentage
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: a dictionary whose keys are the types tests and the value is the maximun percentage
    @rtype: {str: float}
    '''
    types=["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]
    
    percentage_ssc_p=max([e.ssc_p for e in mylist])
    percentage_hsc_p=max([e.hsc_p for e in mylist])
    percentage_degree_p=max([e.degree_p for e in mylist])
    percentage_etest_p=max([e.etest_p for e in mylist])
    percentage_mba_p=max([e.mba_p for e in mylist])
    percentage=[percentage_ssc_p, percentage_hsc_p, percentage_degree_p, percentage_etest_p, percentage_mba_p]

    total=dict(zip(types, percentage))

    return  total

def top5_percentage_working(mylist, n = 5):
    '''
    Given a list of tuples of type Student_number and a parameter, this function returns a dictionary whose keys are the types tests and the value of each key is a list with the five highest percentage
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param n: number of percentage that we want to show in the dictionary
    @type n: int
    @return: a dictionary whose keys are the types tests and the value is the maximun percentage
    @rtype: {str: list[]}
    '''
    types=["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]
    
    percentage_ssc_p=sorted([e.ssc_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_hsc_p=sorted([e.hsc_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_degree_p=sorted([e.degree_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_etest_p=sorted([e.etest_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage_mba_p=sorted([e.mba_p for e in mylist if e.workex == True], reverse=True)[:n]
    percentage=[percentage_ssc_p, percentage_hsc_p, percentage_degree_p, percentage_etest_p, percentage_mba_p]
    
    total=dict(zip(types, percentage))
    return total

def porcentage_working(mylist):
    '''
    Given a list of tuples of type Student_number, this function returns the percentage of people that are currently working
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @return: number of percentage
    @rtype: float
    '''
    working = [e.status for e in mylist if e.status == "Placed"]
    percentage = (len(working)*100)/len(mylist)

    return percentage

def percentage_A(mylist, n = 75.00):
    Given a list of tuples of type Student_number and a parameter, this function returns the percentage of people that pass all the tests with more than 75
    @param mylist: list of tuples with students' data
    @type mylist:  [Student_number(int, str, float, float, str, float, str, float, str, boolean, float, str, float, float, str, datetime. date)]]
    @param n: number of percentage that filter the students
    @type n: float
    @return: number of percentage
    @rtype: float
    A = [e for e in mylist if e.ssc_p >= 75 and e.hsc_p >= n and e.degree_p >= n and e.etest_p >= n and e.mba_p >= n]
    percentage = (len(A)*100)/len(mylist)

    return percentage
