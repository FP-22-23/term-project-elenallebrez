from module1 import *

if __name__ == "__main__":
    students = read_dataset("data/data_set.csv")

    print(students[0:3])
    print(students[-3:])