from module1 import *

if __name__ == "__main__":
    students = read_dataset("data/data_set.csv")

    print(students[0:3])
    print(students[-3:])

def test_hsc_p_filter():
    print(hsc_p_filter(students[:20]))

def test_average_degree_percentage():
    print(average_degree_percentage(students))

def test_order_mba_p_man():
    print(order_mba_p_man(students))

def test_order_mba_p_woman():
    print(order_mba_p_woman(students))

def test_max_degree_p():
    print(max_degree_p(students))
