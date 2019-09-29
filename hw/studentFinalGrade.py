#
#   @author Gabriel Santiago
#   @version 1.0
#   Program will average scores of three grades and properly weighted and calculate the final score
#

#   Declaration of total type double
total = 0.0

print("This program will take grades of weekly assignment, mid-project average and final project average")
print("and calculate the weighted scores to determine the final class grade.")
print("")

#   Prompts to user to enter respective average scores
averageGrade = float(input("Enter Weekly assignment average grade: "))

midProject = float(input("Enter mid-project average: "))

finalProject = float(input("Enter final project average: "))

#   Conversion from percentage to decimal value
aGWeight = 60.0/100.0
mPWeight = 20.0/100.0
fPWeight = 20.0/100.0

#   Takes averages and calculates weighted score percentage
averageGrade = averageGrade * aGWeight

midProject = midProject * mPWeight

finalProject= finalProject * fPWeight

#   Takes the three weighted scores, sums them up to retrieve final score
total = averageGrade + midProject + finalProject;

#   Display to user their final score
print("")
print("Your final grade for the class is:", "{:.2f}".format(total))
