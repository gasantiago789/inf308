#
#   @author Gabriel Santiago
#   @version 1.0
#
#   This Program will open and read a user file. Aftehr the file is read it will capture and store and display
#   each word with the counts of repeat (if any).
#


#   This boolean function will run a try/except statement to verify that the file the user inputs exists. Will return
#   a true or false depending if an error was encountered
#
#   @param NameOfFile This parameter will be the name of the file the user inputs to be verified
#   @returns True/False It will return a true if no errors where encountered and false if an error was encountered
def errorCheck(NameOfFile):
    try:

        #   Name is converted to uppercase to avoid error
        NameOfFile = NameOfFile.upper()

        #   .txt extension is added for automatic error avoidance
        fileName = NameOfFile + ".txt"

        #   Opens and then closes the file.
        finder = open(fileName, "r")
        finder.close()

        return True

    except:
        print("ERROR. FILE DOES NOT EXIST!!\n")
        return False

print("The purpose of this program is to read the file the user input and count the words. This will be printed.\n")
#   Prompts user to input file name
fileName = input("Enter name of file (DO NOT ENTER EXTENSION aka .txt):\n")

#   Will run the function and set either true or false for the boolean "repeat" variable
repeat = errorCheck(fileName)

#   While statement that will ask user to re-input file name until no error is found.
#   This statement will only run if there was an error in the errorCheck() function aka the file name is invalid
while repeat == False:
    fileName = input("Please enter correct name of file:\n")
    repeat = errorCheck(fileName)

'''
    NOTE:
    A function and while method are being used for the error handling of this program since in Python 3, anything that 
    passes through the try/except blocks get deleted. To avoid redundant coding, a function is used. If file opening
    commands where inputed in a try/except statement then the variable would of had to been re-initialized in the main
    scope since it is not stored for external use of the try/except statement. For a more efficient method, use of 
    classes and objects are better.
'''

#   Name is converted to uppercase to avoid error
fileName = fileName.upper()

fileName = fileName + ".txt"

#   Oppening user file type read-only
finder = open(fileName, "r")

#   Init of wordCounter dictionary where words and word count will be stored
wordCounter = {}

#   Loop will remove spaces so they are not counted as a word
for line in finder:
    line = line.strip()

    #   Sets the whole line to lowercase
    line = line.lower()

    #   Splits the word according to a " "
    words = line.split(" ")

    #   For loop that will start storing the words and word count into the dictionary
    #   In this loop, a if/else statement is ran. If the word is repeated then it will add 1 value to the count
    #   otherwise, the word will be set to 1
    for word in words:
        if word in wordCounter:
            wordCounter[word] = wordCounter[word] + 1

        else:
            wordCounter[word] = 1

print("============================================================")

#   For loop that will sort and print the items of the dictionary in a value sorted order.
for key, value in sorted(wordCounter.items(), key=lambda item: item[1], reverse=True):

    #   Will print the items in the dictionary specified as (string - string)
    print("%s - %s" % (key, value))


print("============================================================")

#   Closes the file
finder.close()

