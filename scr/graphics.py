from matplotlib import pyplot as plt

#Block 4

def show_degree_p(mylist):
    year_2010 = [e.degree_p for e in mylist if e.finish_date.year == 2010]
    year_2011 =  [e.degree_p for e in mylist if e.finish_date.year == 2011]
    year_2012 =  [e.degree_p for e in mylist if e.finish_date.year == 2012]
    year_2013 =  [e.degree_p for e in mylist if e.finish_date.year == 2013]
    year_2014 =  [e.degree_p for e in mylist if e.finish_date.year == 2014]
    year_2015 = [ e.degree_p for e in mylist if e.finish_date.year == 2015]
    year_2016 = [e.degree_p for e in mylist if e.finish_date.year == 2016]
    year_2017 = [e.degree_p for e in mylist if e.finish_date.year == 2017]
    year_2018 =  [e.degree_p for e in mylist if e.finish_date.year == 2018]
    year_2019 =  [e.degree_p for e in mylist if e.finish_date.year == 2019]

    average_2010= sum(year_2010)/len(year_2010)
    average_2011 = sum(year_2011)/len(year_2011)
    average_2012 = sum(year_2012)/len(year_2012)
    average_2013 = sum(year_2013)/len(year_2013)
    average_2014 = sum(year_2014)/len(year_2014)
    average_2015 = sum(year_2015)/len(year_2015)
    average_2016 = sum(year_2016)/len(year_2016)
    average_2017 = sum(year_2017)/len(year_2017)
    average_2018 = sum(year_2018)/len(year_2018)
    average_2019 = sum(year_2019)/len(year_2019)

    years=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

    total_average = [average_2010, average_2011, average_2012, average_2013, average_2014, average_2015, average_2016, average_2017, average_2018, average_2019]

    plt.bar(years, total_average)
    plt.xticks(years, years, fontsize=8)
    plt.show()

def show_working(mylist):
    working=[e.status for e in mylist if e.status == "Placed"]
    not_working=[e.status for e in mylist if e.status == "Not Placed"]
    types=["working", "not working"]
    working_num = len(working)
    not_num =len(not_working)
    total= [working_num, not_num]


    plt.pie(total, labels=types)
    plt.show()
