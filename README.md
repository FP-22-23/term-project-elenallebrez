#### Programming term project (Curse 22/23)

Author: Elena Fernández-Llebrez, UVUS: LMX8564

The main propouse of this project is to analayze the data about students in a random campus. 
This data set is publised in this URL (https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement). The original data set has 15 columns, which none of them was a date type. Therefore, I had delete some columns, choosing only 12 out of 15 colummns and I added one columns with dates generated randomly, which it will refer to the date when the student finished the MBA course.

### Structure of the project's folders
- **/src**: It contains the differents Python modules that made up the project
 1. module1.py: It contains the function to analyze the dataset
 2. module1_test.py: It contais the functions tests to prove the function of the module1.
 3. graphics.py: It contains the functions related to graphics

- **/data**: It contains the dataset of the project:
1. data_set.csv: File that contains all the data about the students

### Structure of the data set
Each row contain the data of more or less 200 students, whose names and surnames are unknows.
For each student is registered 13 columns, for that reason the data set is made up by 15 columns:
- **sl_no**: int type, serial number
- **gender**:str type, gender, it can be male(M) or female(F)
- **ssc_p**: float type, Secondary Education percentage-10th Grade
- **hsc_p**:float type, Higher Education percentage-12th Grade
- **hsc_s**:str type, Specialization in Higher Secondary Education
- **degree_p**: float type, Degree Percentage
- **degree_t**: str type, Field of degree education
- **workex**: boolean type, Work experience
- **etest**: float type, Employability test percentage
- **specialisation**: str type, Post Graduation(MBA)-Specialization
- **mba_p**: float type, MBA percentage
- **status**: str type, Status of placement
- **finish_date**: date type, date when they finished the MBA course

### Implemented types
To work with the data from the dataset, I have created a named tuple:

`maintuple=namedtuple("Student_number", "sl_no,gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p,status,finish_date")`

### Implemented functions

#### First delivery
The first function implemented is:
- read_dataset(file): it reads the csv file and returns a list of tuples.

#### Second delivery
In this delivery I have implemented the following functions:

#### Block 1
- preuniversity_p_filter(mylist, p=70.00):Given a list of tuples and a value for the percentage, this function filter the percentage of the higher secondary education. It shows the people who reach and pass the 75%.
- working_students(mylist, work = True, now = "Placed")
- diferent_specialization(mylist)
- average_degree_percentage(mylist): Given a list of tuples, this function returns the value of the sum, the number of students and the average of the total degree percentage.

#### Block 2
- max_degree_p_by_year(mylist, year):Given a list of tuples and a determined year, this function returns the maximun degree percentage of the determined year
- max_min_degree_p(mylist)
- order_mba_p_by_gender(mylist, p=65.0, m ="M", n = 3):Given a list of tuples and a determined gender, this function order a list where it appears the women that reached de 75% of the degree.
- group_hsc_s(mylist)

### Block 3
- number_hsc_s(mylist)
- number_degree_t(mylist)
- number_specialization(mylist)
-  max_number_hsc_s(mylist)
-  max_number_degree_t(mylist)
-  max_number_specialization(mylist)
-  max_percentage(mylist)
-  topn_percentage_working(mylist, n = 5)
-  porcentage_working(mylist)
-  percentage_A(mylist)

### Block 4
- show_degree_p(mylist)
- def show_working(mylist)

### Test module
The following test functions have been defined in the test module, each of which is used to test the function with the same name. 

