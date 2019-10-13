#
#   @author Gabriel Santiago
#   @version 1.0
#
#   This Program will open and read a user CSV file. After the file is read it will capture and store and display
#   each category repetition, and the word count of each repetition.
#

#   Importing of CSV for reading
import csv

#   Method that serves as an error checker
def errorCheck(NameOfFile):
    try:

        #   Name is converted to uppercase to avoid error
        NameOfFile = NameOfFile.upper()

        #   .txt extension is added for automatic error avoidance
        fileName = NameOfFile + ".csv"

        #   Opens and then closes the file.
        finder = open(fileName, "r")
        finder.close()

        return True

    except:
        print("ERROR. FILE DOES NOT EXIST!!\n")
        return False


print("The purpose of this program is to read the CSV file the user input and count the repeated categories and the\n"
      "word count of each category. This will be sorted and printed by value.\n")

#   Prompts user to input file name
fileName = input("Enter name of file (DO NOT ENTER EXTENSION aka .csv):\n")

#   Will run the function and set either true or false for the boolean "repeat" variable
repeat = errorCheck(fileName)

#   While statement that will ask user to re-input file name until no error is found.
#   This statement will only run if there was an error in the errorCheck() function aka the file name is invalid
while repeat == False:
    fileName = input("Please enter correct name of file:\n")
    repeat = errorCheck(fileName)

fileName = fileName.upper()

#  Adds the .csv extension at the end
fileName = fileName + ".csv"

#   Opens the CSV file using ',' as the delimiter
with open(fileName) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    #   Ignores the header and starts directly on the data
    next(readCSV)

    #   Declaration of two dictionaries, one that will store categories with repeated number and another for the words
    categories = {}
    words = {}

    #   Will loop through each rop in the CSV
    for row in readCSV:

        #   Sets the category to the row[2] which is where the category of the news is found
        category = row[2]

        #   Sets the remaining 2 columns together for easier word counting
        row1 = row[0] + " " + row[1]
        row1 = row1.strip("")

        #   Splits each word with a space
        row1 = row1.split(" ")

        #   Counts how long the amount of words are found
        count = len(row1)

        #   Conditional that will count the amount of words found in each category
        if category in words:
            words[category] = words[category] + count
        else:
            words[category] = count

        #   Conditional statements that will count the amount of repetitions of each category
        if category in categories:
            categories[category] = categories[category] + 1

        else:
            categories[category] = 1



print("\nCategory | # of titles | # of words")

#   For loop that will sort by value the dictionary and then will display the category, # of titles and # of words
#   formated into a table with specified spaces.
for key, value in sorted(categories.items(), key=lambda item: item[1], reverse=True):

    #   Formatting to meet table specifications
    print('{:<10}'.format(key), '{:<13}'.format(value), words[key])











