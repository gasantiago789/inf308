#
#   @author Gabriel Santiago
#   @version 1.0
#
#   Program will open CSV file, loop through each category capturing their word count and then calculates the
#   TFIDF and prints a table with top 10 TFIDF values for each category.
#

#   Importing of CSV for reading
import csv

#   Method that will receive the category dictionary and the super dictionary (where ALL words are stored)
#   Will return the new categorized dictionary with TF values
def getTF(categoryDict, wordCount):
    tfDict = {}
    wordCountCount = len(wordCount)
    for word, count in categoryDict.items():
        tfDict[word] = count / (wordCountCount)
    return tfDict

#   Method will get the IDF value for ALL word entries
#   Will return new dictionary with IDF values
def getIDF(documents):
    size = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, value in document.items():    #   Loops through elements
            if value > 0:
                idfDict[word] += 1

    for word, value in idfDict.items():
        idfDict[word] = (size / (value))    #   Actually calculates IDF
    return idfDict

#   Method will calculate and get the TFIDF
#   Will return the new TFIDF dictionary
def getTFIDF(tfCategory, idfs):
    tfidf = {}
    for word, value in tfCategory.items():
        tfidf[word] = value * idfs[word]    #   Calculates TFIDF
    return tfidf


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


print("The purpose of this program is to read a CSV file and show the top 10 TFIDF values in each category.\n")

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

#   Dictionary that will store the words of each category
wordCount = {}
us = {}
opinion = {}
business = {}
newyork = {}
world = {}
magazine = {}
movies = {}
science = {}

#   Opens the CSV file using ',' as the delimiter
with open(fileName) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    #   Ignores the header and starts directly on the data
    next(readCSV)

    for row in readCSV:

        line = row

        '''
        NOTE: THIS MULTI-LINE COMMENT APPLIES FOR ALL OF THE CONDITIONAL STATEMENTS BELLOW
        
        All of these conditional statements will check to see if the selected word exists in the line a.k.a this will
        serve to start storing words with counts in their respective category dictionary.
        
        After it checks which category to work with, it will immediately remove the last entry (which in this case will
        be the text representing the category ex. it will delete 'U.S' from the row).
        
        A loop will run to convert the elements in a string in order to later be split by " " since you can not do this
        for a list and for some reason Python likes to change the type of element without the coder telling it to so 
        this solution is applied to deal with this problem.
        
        Two more loops occur. One stores the word in their individual category dictionary and the second one stores them
        in the super dictionary that stores all the words with their respective count.
        '''
        if 'U.S.' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in us:
                        us[words] = us[words] + 1
                    else:
                        us[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'Opinion' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in opinion:
                        opinion[words] = opinion[words] + 1
                    else:
                        opinion[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'Business' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in business:
                        business[words] = business[words] + 1
                    else:
                        business[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'New York' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in newyork:
                        newyork[words] = newyork[words] + 1
                    else:
                        newyork[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'World' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1
                word = word.split(" ")

                for words in word:
                    if words in world:
                        world[words] = world[words] + 1
                    else:
                        world[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'Magazine' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in magazine:
                        magazine[words] = magazine[words] + 1
                    else:
                        magazine[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'Movies' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in movies:
                        movies[words] = movies[words] + 1
                    else:
                        movies[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1

        elif 'Science' in line:

            line.pop()

            print("\n")

            y = 0
            for x in line:

                word = line[y]
                word = word.lower()
                y += 1

                word = word.split(" ")

                for words in word:
                    if words in science:
                        science[words] = science[words] + 1
                    else:
                        science[words] = 1

                for words in word:
                    if words in wordCount:
                        wordCount[words] = wordCount[words] + 1
                    else:
                        wordCount[words] = 1


#   Gets all of the TF values and copies them back to our scope
usTF = getTF(us, wordCount)
opinionTF = getTF(opinion, wordCount)
businessTF = getTF(business, wordCount)
newyorkTF = getTF(newyork, wordCount)
worldTF = getTF(world, wordCount)
magazineTF = getTF(magazine, wordCount)
moviesTF = getTF(movies, wordCount)
scienceTF = getTF(science, wordCount)

#   Gets the global IDF dictionary and copies it to our main scope
IDF = getIDF([wordCount])

#   Calculates, gets and set the TFIDF value for each category
usTFIDF = getTFIDF(usTF, IDF)
opinionTFIDF = getTFIDF(opinionTF, IDF)
businessTFIDF = getTFIDF(businessTF, IDF)
newyorkTFIDF = getTFIDF(newyorkTF, IDF)
worldTFIDF = getTFIDF(worldTF, IDF)
magazineTFIDF = getTFIDF(magazineTF, IDF)
moviesTFIDF = getTFIDF(moviesTF, IDF)
scienceTFIDF = getTFIDF(scienceTF, IDF)


#   Method that will print the top 10 TFIDF values for each category
#   Since overriding is not done here like Java or C++, the method was made like this to simulate a method polymorphism
#   this case being a method overriding. It will work with 1 or 2 arguments. The second argument is optional but serves
#   as a modifier if a user wishes to automatically add a "\n" after printing the list
def showTable(x, mod=None):
    num = 1
    if mod is not None:
        for key, value in sorted(x.items(), key=lambda item: item[1], reverse=True)[:10]: # This works as range
            print(num,":",key, " - ", "{0:.5f}".format(value))
            num += 1
        print(mod)

    else:
        for key, value in sorted(x.items(), key=lambda item: item[1], reverse=True)[:10]:
            print(key, " - ", "{0:.5f}".format(value))

#   Prints each categorized TFIDF table
print("=========================")
print("US: TF-IDF\n")
showTable(usTFIDF, "\n")

print("=========================")
print("Opinion: TF-IDF\n")
showTable(opinionTFIDF, "\n")

print("=========================")
print("Business: TF-IDF\n")
showTable(businessTFIDF, "\n")

print("=========================")
print("New York: TF-IDF\n")
showTable(newyorkTFIDF, "\n")

print("=========================")
print("World: TF-IDF\n")
showTable(worldTFIDF, "\n")

print("=========================")
print("Magazine: TF-IDF\n")
showTable(magazineTFIDF, "\n")

print("=========================")
print("Movies: TF-IDF\n")
showTable(moviesTFIDF, "\n")

print("=========================")
print("Science: TF-IDF\n")
showTable(scienceTFIDF, "\n")

