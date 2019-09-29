#
#   @author Gabriel Santiago
#   @version 1.0
#
#   This program will take a user input, count the letters entered and organize a list on screen with the letters
#   that are presented.
#

#   Prompt user purpose of program
print("This program will take a string of characters input and display the characters with each letter count\n\n")

#   Prompt user
word = input("Please enter a string: ");

#   Makes the letters uppercase automatically so that they are counted as the same
word = word.upper()

#   Creation of dictionary where ordered letters and numbers will be placed
dict = {}

#   For loop that loops thorugh the string and ads values on to it depending if the letter is repeated or not
for x in word:
    keys = dict.keys()
    if x in keys:
        dict[x] += 1
    else:
        dict[x] = 1

#   Displays the string with letters counted and sorted by value
print("\n")
print("============================================================================================================")
print("SORTED BY VALUE AND ORIGINAL ENTERED ORDER OF CHARACTERS")
for x in dict.keys():
    print(x, ':', dict[x])

print("============================================================================================================")


