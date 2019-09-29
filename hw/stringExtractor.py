#
#   @author Gabriel Santiago
#   @version 1.0
#
#   Program will take user input and extract ONLY string characters, not special characters. It will also display this
#   string of character in lower case form.
#

#   Importation of regular expressions
import re

#   Display goal of program
print("The goal of this program is for the user to enter a string of characters and it will only extract the actual\n"
      "string characters in the line excluding special character such as !@@##$%$%^&^& and lowercase")

#   Prompt user to enter string of character and store it into userInput variable type string (BY DEFAULT)
userInput = input("Please enter any text, when you are done press the SPACE key: \n")

#   Storing new string using regular expressions findall method which will only find lower case and
#   uppercase characters that range from A to Z.
userInput = " ".join(re.findall("[a-zA-z]+", userInput))

#   Display new extracted string of character using .lower() to display it in lowercase letters
print(userInput.lower())