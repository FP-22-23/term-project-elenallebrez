#### Programming term project (Curse 22/23)

Author: Elena Fernández-Llebrez, uvus: LMX8564

The main propouse of this project is to analayze the data about students in a random campus. 
This data set is publised in this URL (https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement). The original data set has 15 columns, which none of them was a date type. Therefore, I had delete some columns, choosing only 12 out of 15 colummns and I added one columns with dates generated randomly, which it will refer to the date when the student finished the MBA course.

### Structure of the project's folders
- **/src**: It contains the differents Python modules that made up the project
 1. module1.py: It contains the function to analyze the dataset
 2. module1_test.py: It contais the functions tests to prove the function of the module1.

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
## First delivery
The first function implemented is:
- read_dataset(file): it reads the csv file and returns a list of tuples.

## Second delivery
In this delivery I have implemented the following functions:
- hsc_p_filter(list, p=7500.0)
- average_degree_percentage(list)
- order_mba_p_man(list, p=7500, m ="M")
- order_mba_p_woman(list, p=7500.0, f ="F")
