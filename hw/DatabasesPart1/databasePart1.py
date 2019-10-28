#
#   @author Gabriel Santiago
#   @version 1.0
#

import sqlite3
import random

conn = sqlite3.connect('studentDatabase1.sqlite')
cur = conn.cursor()


#   For the first run, comment this line
cur.execute('CREATE TABLE "studentDatabase1" ( "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "firstName" TEXT, "lastName" TEXT, "class" TEXT, "major" TEXT, "minor" TEXT );')


studentCount = 0

studentCount = int(input("Enter the amount of undergraduate students: "))
idSetter = 100001

#   After first run, comment this whole block

for x in range(0, studentCount):
    print(idSetter)
    cur.execute('INSERT INTO studentDatabase1 (id) VALUES (?);', (idSetter,))
    conn.commit()
    idSetter += 1

firstName = open('firstnames.txt', "r")
lastName = open('surnames.txt', "r")
className = open('class.txt', "r")
major = open('departments.txt', "r")

name = []
last = []
classN = []
majorLaser = []

for line in firstName:
    name.append(line.strip())

for line in lastName:
    last.append(line.strip())

for line in className:
    classN.append(line.strip())

for line in major:
    majorLaser.append(line.strip())


for x in range (0, studentCount):
    randomNum = random.randint(0, len(name)-1)
    randomName = name[randomNum]

    cur.execute('UPDATE studentDatabase1 SET firstName = ? where id = ?;', (randomName, idSetter))
    idSetter += 1
    conn.commit()



for x in range(0, studentCount):
    randomNum = random.randint(0, len(last)-1)
    randomName = last[randomNum]

    cur.execute('UPDATE studentDatabase1 SET lastName = ? where id = ?;', (randomName, idSetter))
    idSetter += 1
    conn.commit()



for x in range(0, studentCount):
    randomNum = random.randint(0, len(classN)-1)
    randomName = classN[randomNum]

    cur.execute('UPDATE studentDatabase1 SET class = ? where id = ?;', (randomName, idSetter))
    idSetter += 1
    conn.commit()



for x in range(0, studentCount):
    randomNum = random.randint(0, len(majorLaser)-1)
    randomName = majorLaser[randomNum]

    cur.execute('UPDATE studentDatabase1 SET major = ? where id = ?;', (randomName, idSetter))
    idSetter += 1
    conn.commit()



for x in range(0, studentCount):
    randomNum = random.randint(0, len(majorLaser)-1)
    randomName = majorLaser[randomNum]

    cur.execute('UPDATE studentDatabase1 SET minor = ? where id = ?;', (randomName, idSetter))
    idSetter += 1
    conn.commit()


choice = 0
print("\nEnter the respective number to choose an action\n1. View\n2. Modify\n3. Add\n4. Summarize\n")
choice = int(input())
repeat = False

if choice == 1:
    idNum = input("Please enter the id number: ")
    idlist2 = []
    cur.execute('SELECT id FROM studentDatabase1')
    idlist = cur.fetchall()
    for t in idlist:
        for x in t:
            idlist2.append(x)

    cur.execute('SELECT * FROM studentDatabase1 WHERE id=?', (idNum,))
    data = cur.fetchall()
    data2 = []
    for t in data:
        for x in t:
            data2.append(x)

    for x in data2:
        print(x)


if choice == 2:
    idNum = input("Please enter the id number: ")
    idlist2 = []
    cur.execute('SELECT id FROM studentDatabase1')
    idlist = cur.fetchall()
    for t in idlist:
        for x in t:
            idlist2.append(x)

    print("What would you like to modify?")
    print("1. Fist Name")
    print("2. Last Name")
    print("3. Class")
    print("4. Major")
    print("5. Minor\n")
    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        newName = input("Enter the new Name ")
        cur.execute('UPDATE studentDatabase1 SET firstName = ? where id = ?;', (newName, idNum))
        conn.commit()
    if choice2 == 2:
        newLast = input("Enter the new Last name ")
        cur.execute('UPDATE studentDatabase1 SET lastName = ? where id = ?;', (newLast, idNum))
        conn.commit()
    if choice2 == 3:
        newClass = input("Enter the new Class ")
        cur.execute('UPDATE studentDatabase1 SET class = ? where id = ?;', (newClass, idNum))
        conn.commit()
    if choice2 == 4:
        newMajor = input("Enter the new Major ")
        cur.execute('UPDATE studentDatabase1 SET major = ? where id = ?;', (newMajor, idNum))
        conn.commit()
    if choice2 == 5:
        newMinor = input("Enter the new Minor ")
        cur.execute('UPDATE studentDatabase1 SET minor = ? where id = ?;', (newMinor, idNum))
        conn.commit()


if choice == 3:
    print("ADD data to the Database")
    #   There is no need to add an ID number since the ID colum in database is set to AUTOINCREMENT
    newName = input("Enter the new Name: ")
    newLast = input("Enter the new Last Name")
    newClass = input("Enter the new Class name")
    newMajor = input("Enter the new Major")
    newMinor = input("Enter the new Minor")
    cur.execute('INSERT INTO studentDatabase1 (firstName, lastName, class, major, minor) VALUES (?, ?, ?, ?, ?);', (newName, newLast, newClass, newMajor, newMinor))
    #   If "Database is locked" Error is executed then upon research it is a SQLite problem not because of the code
    #   This same SQL query was ran in SQL lite and it worked
    conn.commit()

if choice == 4:
    cur.execute('SELECT firstName from studentDatabase1 ORDER BY major AND minor')
    list1 = cur.fetchall()
    list2 = []
    for t in list1:
        for x in t:
            list2.append(x)

    for x in (list2):
        print(x)
