#
#   @author Gabriel Santiago
#   @version 1.0
#   Program will take the users participation quantity, min and max age and will randomly generate the quantity of
#   males and females with their respective ages with the set boundaries of minimum and maximum
#

#   Import of the random module to use respective methods
import random

#   Display purpose of program to user
print("The software will will randomly assign participants to a study including their gender and age\n")

#   Captures quantity of participants user enters
#   Sets that entered value to an integer (also for min and max)
participantNumber = int(input("Please enter the number of participants in the study: "))

#   Captures minimum and maximum age
minAge = int(input("Enter the minimum age of participants: "))

maxAge = int(input("Enter the maximum age of participants: "))

#   Declaration of count, male and female quantity
count = 0
maleQua = 0
femQua = 0

#   Loop will retrieve the quantity of males and females of the entered participant quantity
#   Once count reaches the same number of participants, it will make the while false breaking and continuing rest of code
while count < participantNumber:

    #   Retrieves random integer 1 for male and 2 for female
    quan = random.randint(1, 2)

    #   Condition that if quan is 1 then it will add sum 1 to the male
    if quan == 1:
        maleQua += 1
        count += 1

    #   Condition that if quan is not 2 (a.k.a in this case 2) then it will add 1 to the female quantity
    else:
        count += 1
        femQua += 1

#   Definition of method that will set ages to participants and get the average ages of participants
#
#   @param quantity Is the quantity of participants that will enter the method
#   @param min Is the minimum age that will pass in to the method
#   @param max Is The maximum age that will pass in to the method
#   @return Will return the average ages of the participants
def getAgeAvrg(quantity, min, max):
    count = 0
    ageSum = 0

    #   As long as quantity is not equal to 0 (will be reduced by 1 each loop)
    while quantity != 0:

        #   Will randomly set an age following the parameters
        age = random.randint(min, max)
        count += 1

        #   Sums the ages
        ageSum += age

        #   This will serve as a negative counter since it will go down until reaching 0 thus ending the loop
        quantity -= 1

    #   Calculates and returns the average age
    return ageSum / count

#   Using the male quantity and min and max age, it will determine the ages of each male and calculate the average
maleAvAge = getAgeAvrg(maleQua, minAge, maxAge)

#   Using the female quantity and min and max age, it will determine the ages of each female and calculate the average
femAvAge = getAgeAvrg(femQua, minAge, maxAge)


#   Prints out formated quantities of male and female with their respective average ages
print("\nMales: ", maleQua, " Avg. Age: ", format(maleAvAge, "0,.0f"))

print("Females: ", femQua, " Avg. Age: ", format(femAvAge, "0,.0f"))

