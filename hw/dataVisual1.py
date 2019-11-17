#
#   @author Gabriel Santiago
#   @version 1.0
#
#   Program will take the user input and throw a graph with the percentage entered.
#

from graphics import *

print("This program will take two values (decimal or percentage) and will throw a vertical graph\n")
number = float(input("Hello. Please enter a numeric value. Value must be in percentage of decimal for bar 1: "))

number2 = float(input("Enter another number for bar 2: "))

#   Creates the window itself
win = GraphWin("Data Visualization 1", 150, 150)

#   Sets the coordinates so they work normally opposed to the reversed Y pane
win.setCoords(0, 0, 150, 150)

#   Sets the windows background to white
win.setBackground('white')

#   If the number is less than 1 then it is a decimal which needs to be changed to a percentage value
if number < 1:
    number = number * 100
    number = number + 100
    number = int(number)
    print(number)

if number2 < 1:
    number = number * 100
    number = number + 100
    number = int(number)
    print(number)

#   X and Y pane
ln = Line(Point(10, 10), Point(100, 10))
ln.setOutline('black')
ln.draw(win)

ln2 = Line(Point(10, 10), Point(10, 100))
ln2.setOutline('black')
ln2.draw(win)

#   Grey lines in the graph
gln = Line(Point(10, 20), Point(100, 20))
gln.setOutline('lightgrey')
gln.draw(win)

gln2 = Line(Point(10, 30), Point(100, 30))
gln2.setOutline('lightgrey')
gln2.draw(win)

gln3 = Line(Point(10, 40), Point(100, 40))
gln3.setOutline('lightgrey')
gln3.draw(win)

gln4 = Line(Point(10, 50), Point(100, 50))
gln4.setOutline('lightgrey')
gln4.draw(win)

gln5 = Line(Point(10, 60), Point(100, 60))
gln5.setOutline('lightgrey')
gln5.draw(win)

gln6 = Line(Point(10, 70), Point(100, 70))
gln6.setOutline('lightgrey')
gln6.draw(win)

gln7 = Line(Point(10, 80), Point(100, 80))
gln7.setOutline('lightgrey')
gln7.draw(win)

gln8 = Line(Point(10, 90), Point(100, 90))
gln8.setOutline('lightgrey')
gln8.draw(win)

gln9 = Line(Point(10, 100), Point(100, 100))
gln9.setOutline('lightgrey')
gln9.draw(win)

#   Legend of the graph
littleRec = Rectangle(Point(10, 105), Point(25, 120))
littleRec.setFill('red')
littleRec.draw(win)

txt = Text(Point(45, 110), "Bar 1")
txt.draw(win)

littleRec1 = Rectangle(Point(60, 105), Point(75, 120))
littleRec1.setFill('blue')
littleRec1.draw(win)

txt2 = Text(Point(95, 110), "Bar 2")
txt2.draw(win)

#   Bar 1
bar1 = Rectangle(Point(20, 10), Point(30, number))
bar1.setFill('red')
bar1.draw(win)

#   Value 1 entered
txt3 = Text(Point(20, 130), number)
txt3.setSize(8)
txt3.draw(win)

#   Value 2 entered
txt4 = Text(Point(68, 130), number2)
txt4.setSize(8)
txt4.draw(win)

#   Bar 2
bar2 = Rectangle(Point(40, 10), Point(50, number2))
bar2.setFill('blue')
bar2.draw(win)



win.getMouse()
win.close()
