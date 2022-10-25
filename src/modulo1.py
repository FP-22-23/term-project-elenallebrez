from collections import namedtuple

import csv

maintuple=namedtuple("Number", "n, gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status, salary")

def read_placement_data_full_class(file):
    with open(file, "r", encoding = "utf-8") as f:
        reader=csv.reader(f)
        next(reader)
        students=[maintuple(int(n), gender, float(ssc_p), ssc_b, float(hsc_p), hsc_b, hsc_s, float(degree_p), degree_t, workex, float(etest_p), specialisation, float(mba_p), status, salary)
        for n, gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status, salary in reader ]

    return students
