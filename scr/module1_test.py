from module1 import *

def test_preuniversity_p_filter(mylist, p=70.00):
    sol = preuniversity_p_filter(mylist, p=70.00)
    sol1 = preuniversity_p_filter(mylist, p=60.00)
    sol_5 = sol[:5]
    sol1_5 = sol1[:5]
    print("These are the studets that has more than the percentage you want(70 default)", sol_5)
    print("These are the studets that has more than the percentage 60.00", sol1_5)

def test_working_students(mylist, work = True, now = "Placed"):
    sol = working_students(mylist, work = True, now = "Placed")
    sol_5 = sol[:5]
    sol1 = working_students(mylist, work = False, now = "Not Placed")
    sol1_5 = sol1[:5]
    print("These are the students that has working experience and are currently working(default)", sol_5)
    print("These are the students that has no working experience and aren't currently working(default)", sol1_5)

def test_diferent_specialization(mylist):
    sol = diferent_specialization (mylist)
    print("The specializations in highschool are: ", sol[0], " the specializations in degree are: ", sol[1], " the specializations in master are: ",  sol[2])


def test_average_degree_percentage(mylist):
    sol = average_degree_percentage(mylist)
    print("The total sum of the degree percentage is: ", sol[0], " the total number of students is: ", sol[1], " so, the average is: ", sol[2])


def test_max_degree_p_by_year(mylist, year):
    sol = max_degree_p_by_year(mylist, year)
    print("These is the student that is currently working and has the maximun degree percentage in that year", sol)


def test_max_min_degree_p(mylist):
    sol = max_min_degree_p(mylist)
    print("The students with the highest degree percentage is: ", sol[0], " and the students with the lowest degree percentage is: ", sol[1])


def test_order_mba_p_by_gender(mylist, p=65.0, m ="M", n = 3):
    sol = order_mba_p_by_gender(mylist, p=65.0, m ="M", n = 3)
    print("These are the three male students that has the highest degree percentage", sol)
    sol1 = order_mba_p_by_gender(mylist, p=65.0, m ="F", n = 3)
    print("These are the three female students that has the highest degree percentage", sol)


def test_group_hsc_s(mylist):
    sol = group_hsc_s(mylist)
    print( "These are the students that chose each specialization", sol)


def test_number_hsc_s(mylist):
    sol = number_hsc_s(mylist)
    print("These are the number of students that chose each specialization in highschool", sol)


def test_number_degree_t(mylist):
    sol = number_degree_t(mylist)
    print("These are the number of students that chose each specialization in the degree", sol)


def test_number_specialization(mylist):
    sol = number_specialization(mylist)
    print("These are the number of students that chose each specialization in the master", sol)


def test_max_number_hsc_s(mylist):
    sol = max_number_hsc_s(mylist)
    print("This is the highschool specialization which has more students", sol)


def test_max_number_degree_t(mylist):
    sol = max_number_degree_t(mylist)
    print("This is the degree specialization which has more students", sol)


def test_max_number_specialization(mylist):
    sol = max_number_specialization(mylist)
    print("This is the master specialization which has more students", sol)


def test_max_percentage(mylist):
    sol = max_percentage(mylist)
    print("These are the maximun percentage in each test", sol)


def test_topn_percentage_working(mylist, n = 5):
    sol = topn_percentage_working(mylist, n = 5)
    print("These are the top 5(default) percentage in each test that are now working", sol)
    sol1 = topn_percentage_working(mylist, n = 3)
    print("These are the top 3 percentage in each test that are now working", sol1)

def test_porcentage_working(mylist):
    sol = porcentage_working(mylist)
    print("This is the percentage of students that are working: ",sol, "%")

def test_percentage_A(mylist):
    sol=percentage_A(mylist)
    print("This is percentage of students that has more than 75 in all the test: ", sol)
    

def main():
    print (25*"-"+"test_preuniversity_p_filter" +"-"*25)
    test_preuniversity_p_filter(students)
    preuniversity_p_filter(students, p=50.00)

    print(25*"-"+"test_working_students" +"-"*25)
    test_working_students(students)

    print(25*"-"+"test_diferent_specialization" +"-"*25)
    test_diferent_specialization(students)

    print(25*"-"+"test_average_degree_percentage" +"-"*25)
    test_average_degree_percentage(students)

    print(25*"-"+"test_max_degree_p_by_year" +"-"*25)
    test_max_degree_p_by_year(students, 2010)
    test_max_degree_p_by_year(students, 2019)

    print(25*"-"+"test_max_min_degree_p"+"-"*25)
    test_max_min_degree_p(students)

    print(25*"-"+"test_order_mba_p_by_gender" +"-"*25)
    test_order_mba_p_by_gender(students)

    print(25*"-"+"test_group_hsc_s" +"-"*25)
    test_group_hsc_s(students)

    print(25*"-"+"test_number_hsc_s"+"-"*25)
    test_number_hsc_s(students)

    print(25*"-"+"test_number_degree_t" +"-"*25)
    test_number_degree_t(students)

    print(25*"-"+"test_number_specialization" +"-"*25)
    test_number_specialization(students)

    print(25*"-"+"test_max_number_hsc_s" +"-"*25)
    test_max_number_hsc_s(students)

    print(25*"-"+"test_max_number_degree_t" +"-"*25)
    test_max_number_degree_t(students)

    print(25*"-"+"test_max_number_specialization" +"-"*25)
    test_max_number_specialization(students)

    print(25*"-"+"test_max_percentage" +"-"*25)
    test_max_percentage(students)

    print(25*"-"+"test_topn_percentage_working "+"-"*25)
    test_topn_percentage_working(students)

    print(25*"-"+"test_porcentage_working "+"-"*25)
    test_porcentage_working(students)

    print(25*"-"+"test_percentage_A "+"-"*25)
    test_percentage_A(students)

if __name__ == "__main__":
    students = read_dataset("data/data_set.csv")
    print(students[0:3])
    print(students[-3:])
    main()
