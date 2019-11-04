#
#   @author Gabriel Santiago
#   @version 1.0
#

import sqlite3
import random

'''
    This program will ask user for choice inputs, create a database with two tables, read information from 
    a current database, calculate the average of all of the students in an informatics course and then will 
    list and display Senior students taking informatics
'''
conn = sqlite3.connect('studentDB.sqlite')
cur = conn.cursor()
conn2 = sqlite3.connect('wa9-students.sqlite')
cur2 = conn2.cursor()

#   Prompts user to enter a choice. User should input yes for this if there is no current database created
print("Welcome to StudentDB terminal!!!\n")
choice1 = input("Starting 'inf108'... Was the table already created? Y/N\n")
choice1 = choice1.upper()

if choice1 == 'N':
    cur.execute('CREATE TABLE "inf108" ("id" INTEGER NOT NULL PRIMARY KEY, "grade" INTEGER, "year" integer)')
    print("Table 'inf108' was created!\n")

#   Lists for capturing data from database
inf108idList_raw = []
inf108idList = []
inf108ClassList_raw = []
inf108ClassList = []
cur2.execute('select "id" from students where Major="Informatics" or Minor="Informatics"')
inf108idList_raw = cur2.fetchall()
cur2.execute('select year from students where Major="Informatics" or Minor="Informatics"')
inf108ClassList_raw = cur2.fetchall()


#   Removes the (element,) comma from the list
for i in inf108idList_raw:
    inf108idList.append(i[0])

for i in inf108ClassList_raw:
    inf108ClassList.append(i[0])

#   Asks user if they want to add the data into the data, user should enter N if the data is already on the table
choice2 = input("Do you wanna insert the id's with random grades into 'inf108'? Y/N\n")
choice2 = choice2.upper()
if choice2 == 'Y':
    #   For loop inserting data to new table
    for x in range(0, len(inf108idList)):
        randNum = round(random.uniform(0.0, 4.0), 1)
        value = inf108idList[x]
        year = inf108ClassList[x]
        cur.execute('insert into inf108 (id, grade, year) values (?, ?, ?);', (value, randNum, year,))
        conn.commit()

#   Ask user if they wanna create the new table 308. User should input N if the table already exists
choice3 = input("Did you already create 'inf308' table in 'studentDB'? Y/N\n")
choice3 = choice3.upper()
if choice3 == 'N':
    cur.execute('CREATE table "inf308" ("id" integer NOT NULL PRIMARY KEY, "name" text, "grade" integer, "year" text)')
    print("Table 'inf308' was created!\n")

#   308 Sql capture lists
inf308idList_raw = []
inf308idList = []
inf308NameList_raw = []
inf308NameList = []
inf308ClassList_raw = []
inf308ClassList = []

cur2.execute('select id from students where (year="Junior" or year="Senior") and (Major="Informatics" or Minor="Informatics")')
inf308idList_raw = cur2.fetchall()
cur2.execute('select Firstname from students where (year="Junior" or year="Senior") and (Major="Informatics" or Minor="Informatics")')
inf308NameList_raw = cur2.fetchall()
cur2.execute('select year from students where (year="Junior" or year="Senior") and (Major="Informatics" or Minor="Informatics")')
inf308ClassList_raw = cur2.fetchall()

#   Removes the (element,) comma from the list
for i in inf308idList_raw:
    inf308idList.append(i[0])

#   Removes the (element,) comma from the list
for i in inf308NameList_raw:
    inf308NameList.append(i[0])

for i in inf308ClassList_raw:
    inf308ClassList.append(i[0])

#   Ask inputs if they wanna insert data to new table 308, if data already there then user should answer N
choice4 = input("Do you wanna insert the id's with random grades into 'inf308'? Y/N\n")
choice4 = choice4.upper()
if choice4 == 'Y':
    for x in range(0, len(inf308idList)):
        randNum = round(random.uniform(0.0, 4.0), 1)
        value = inf308idList[x]
        name = inf308NameList[x]
        year = inf308ClassList[x]
        cur.execute('insert into inf308 (id, name, grade, year) values (?, ?, ?, ?);', (value, name, randNum, year,))
        conn.commit()

list_raw = []
cur.execute('select * from inf108')
list_raw = cur.fetchall()
list = []

list2_raw = []
cur.execute('select * from inf308')
list2_raw = cur.fetchall()
list2 = []

for i in list_raw:
    list.append(i[1])

for i in list2_raw:
    list2.append(i[2])



total = 0
total2 = 0
total2 = int(total2)
for x in list:
    total += x



for x in list2:
    total2 += x

#   Calculates the average of all the informatic grades
print("\n=============================================================")
print("Total 1: ", total)
print("Total 2: ", total2)
finalTotal = total + total2
print("Final total: ", finalTotal)

print("Total length: ", len(list)+len(list2))
totalLen = len(list)+len(list2)
avg = finalTotal / totalLen
avg = round(avg, 2)
print("AVG = ", avg)
print("=============================================================")

#   Function that calculates average between to grades
def calcAvg(a, b):
    subtotal = a + b
    avg = subtotal / 2
    return round(avg, 2)

#   SQL lists
number_raw = []
number2_raw = []
number = []
number2 = []
names_raw = []
names = []
idList_raw = []
idList = []
majors_raw = []
majors = []
minors_raw = []
minors = []
grade1_raw = []
grade1 = []
grade2_raw = []
grade2 = []
cur.execute('select grade from inf108 where year="Senior"')
number_raw = cur.fetchall()
cur.execute('select grade from inf308 where year="Senior"')
number2_raw = cur.fetchall()
cur.execute('select name from inf308 where year="Senior"')
names_raw = cur.fetchall()
cur.execute('select id from inf308 where year="Senior"')
idList_raw = cur.fetchall()
cur2.execute('select Major from students where (year="Junior" or year="Senior") and (Major="Informatics" or Minor="Informatics");')
majors_raw = cur2.fetchall()
cur2.execute('select Minor from students where (year="Junior" or year="Senior") and (Major="Informatics" or Minor="Informatics");')
minors_raw = cur2.fetchall()
cur.execute('select grade from inf108 where year="Senior";')
grade1_raw = cur.fetchall()
cur.execute('select grade from inf308 where year="Senior"')
grade2_raw = cur.fetchall()

for i in grade1_raw:
    grade1.append(i[0])

for i in grade2_raw:
    grade2.append(i[0])

for i in number_raw:
    number.append(i[0])

for i in number2_raw:
    number2.append(i[0])

for i in names_raw:
    names.append(i[0])

for i in idList_raw:
    idList.append(i[0])

for i in majors_raw:
    majors.append(i[0])

for i in minors_raw:
    minors.append(i[0])

#   Display table with values
print('{:^10}'.format("\n\t\t\t\tSENIOR STUDENTS TAKING INFORMATICS"))
print("==========================================================================")
print('{:s}'.format("ID"), '{:^20}'.format("Name"), '{:^0}'.format("Major"), '{:^38}'.format("Minor"), '{:^0}'.format("AVG"))
print("==========================================================================")
for x in range(0, len(idList)):
    print('{:d}'.format(idList[x]), '{:^13}'.format(names[x]), '{:^13}'.format(majors[x]), '{:^30}'.format(minors[x]), '{:^10}'.format(calcAvg(grade1[x], grade2[x])))
    print("--------------------------------------------------------------------------")
