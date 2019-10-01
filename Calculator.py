from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import math
import random
from time import gmtime, strftime

# <editor-fold desc="Config">
# Configuration for colours
bgcolour = "black"
fgcolour = "white"
buttonbgcolour = "red"
buttonfgcolour = "white"
backgroundcolour = "grey"
xlabel = 100

# </editor-fold>

# <editor-fold desc="Creating the GUI">
# Creates the GUI
root = tk.Tk()

# Creates the notebook (nb)
nb = ttk.Notebook(root)

# Adding pages to the notebook (nb)
page1 = tk.Frame(nb)
page2 = tk.Frame(nb)
page3 = tk.Frame(nb)
page4 = tk.Frame(nb)
page5 = tk.Frame(nb)
page6 = tk.Frame(nb)

# Colouring the page
page1.config(bg=backgroundcolour)
page2.config(bg=backgroundcolour)
page3.config(bg=backgroundcolour)
page4.config(bg=backgroundcolour)
page5.config(bg=backgroundcolour)
page6.config(bg=backgroundcolour)

# Naming the pages
nb.add(page1, text='Areas')
nb.add(page2, text='RandNumGen')
nb.add(page3, text='Shapes')
nb.add(page4, text='Draw')
nb.add(page5, text='Flappy')
nb.add(page6, text='Snake')

# Packing pages
nb.pack(expand=1, fill="both")

# Configuring the GUI
# Size
root.geometry("285x500")

# Makes the GUI always be on the top
root.attributes("-topmost", True)


# This function updates the title of the GUI to have the current date and time
def updateGUI():

    # Retrieves the current hour
    hour = strftime("%H", gmtime())

    # Subtracts by 5 to make it our timezone
    hour = (int(hour)-5)

    # Checks to see if it is PM or AM
    if int(hour) >= 12 or int(hour) < 0:
        pmam = "PM"
    else:
        pmam = "AM"

    # Makes the 24 hour clock a 12 hour clock
    hour %= 12

    # Makes it so instead of using 0 it uses 12 at mid day and mid night
    if int(hour) == 0:
        hour = 12
    # Converts to str so it can be displayed
    hour = str(hour)

    # Changes the title to the time and date
    root.title(strftime("%a, %d %b "+hour+":%M "+pmam, gmtime()))

    # Makes it update every 1000 milliseconds/1 second
    root.after(1000,updateGUI)

# Calls the function to get it going
updateGUI()

# </editor-fold>

# <editor-fold desc= "Functions">

# Checks if a variable is an int if not it prints "Not an Integer"
def isint(s):
    try:
        s= int(s)
    except:
        print("Not an Integer")

#  Checks if a variable is a float if not it prints "Not a Float"
def isfloat(s):
    try:
        s = float(s)
    except:
        print("Not a Float")

# Does a selection sort with a list given returns sorted list
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

# Does a bubble sort not as effective as a selection sort (no longer in use)
def bubSort(l):
    listlen = len(l)
    for k in range((listlen) - 1, 0, -1):
        for i in range(k):
            if l[i] > l[i + 1]:
                num = l[i]
                l[i] = l[i + 1]
                l[i + 1] = num

# Displays all random numbers sorted
def sortran():
    selectionSort(ranlist)
    displayran.config(state="normal")
    displayran.delete(1.0,END)
    displayran.config(state="disable")
    for i in range(rangeofran):
        displayran.config(state="normal")
        displayran.insert(END, "Random Number: " + str(ranlist[i]) + "\n\n")
        displayran.config(state="disable")


# Checks whether a number is a float or int
def int_or_float(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

#</editor-fold>

# <editor-fold desc="Page 1 Code">

# PAGE 1 FUNCTIONS
# ***********************************************************************************************************************


# This code runs when the Rectangle button is pressed it places entries and labels for length and width
def rect():

    root.unbind_all(root)
    root.bind("<Return>", run)

    #placing the labels and entry boxes
    lengthlabel.place(x=xlabel+16, y=65)
    lengthentry.place(x=xlabel-22, y=85)
    widthlabel.place(x=xlabel + 16, y=110)
    widthentry.place(x=xlabel - 22, y=130)
    # this will set the button to disabled so it cannot be clicked again as well as it will reset the other buttons
    Rectangle.config(state="disable", )
    Circle.config(state="normal")
    Triangle.config(state="normal")
    # removes the labels that rectangle does not need
    radiuslabel.place_forget()
    radiusentry.place_forget()
    heightentry.place_forget()
    heightlabel.place_forget()
    baselabel.place_forget()
    baseentry.place_forget()
    # tells the program which shape to calculate
    global calccirc, calctri, calcrect
    calcrect=True
    calctri=False
    calccirc=False


# This code runs when the circle button is pressed it places entries and labels for radius
def circ(*args):

    # Unbinds and rebinds to prevent other bindings from interfering.
    root.unbind_all(root)
    root.bind("<Return>", run)

    # Places the label and entry box
    radiuslabel.place(x=xlabel + 16, y=65)
    radiusentry.place(x=xlabel - 22, y=85)

    # Buttons again but this time for Circle.
    Rectangle.config(state="normal")
    Circle.config(state="disable")
    Triangle.config(state="normal")

    # Removes labels and entries to make room for radius
    lengthlabel.place_forget()
    lengthentry.place_forget()
    heightentry.place_forget()
    heightlabel.place_forget()
    widthentry.place_forget()
    widthlabel.place_forget()
    baselabel.place_forget()
    baseentry.place_forget()

    # Tells the program which shape to calculate
    global calccirc, calctri, calcrect
    calcrect = False
    calccirc = True
    calctri = False


# This code runs when the Triangle button is pressed it places entries and labels for base and height
def tri(*args):

    # Unbinds and rebinds to prevent other bindings from interfering.
    root.unbind_all(root)
    root.bind("<Return>", run)

    # Places labels and entrys for Triangle
    heightlabel.place(x=xlabel + 16, y=65)
    heightentry.place(x=xlabel - 22, y=85)
    baselabel.place(x=xlabel + 16, y=110)
    baseentry.place(x=xlabel - 22, y=130)

    # Buttons once again (Triangle)
    Rectangle.config(state="normal")
    Triangle.config(state="disable")
    Circle.config(state="normal")

    # Removes other labels that are in the way
    lengthlabel.place_forget()
    lengthentry.place_forget()
    widthentry.place_forget()
    widthlabel.place_forget()
    radiusentry.place_forget()
    radiuslabel.place_forget()

    # Tells the program which shape to calculate
    global calccirc,calctri,calcrect
    calccirc = False
    calcrect = False
    calctri = True


# This code runs when the run button is pressed it begins the calculations
def run(*args):

    # Calculates the rectangle area and perimeter
    if calcrect:

        # Putting the entries into a float variable
        length = float(lengthentry.get())
        width = float(widthentry.get())

        # Math to calculate area and perimeter of the rectangle
        rectarea=length*width
        rectperim=length*2+width*2

        # Outputs the results to the display box
        displayBox.config(state="normal")  # makes it so the box is editable
        displayBox.insert(END, "Rectangle Area: "+ str(rectarea)+"u Sq\n")
        displayBox.insert(END, "Rectangle Perimeter: "+ str(rectperim) + "u Sq\n\n")
        displayBox.config(state="disable")  # makes it so you cannot edit it

    # Calculates the triangle area
    if calctri:

        # Putting entries into float variables
        height = float(heightentry.get())
        base = float(baseentry.get())

        # Doing math to get the area of the triangle
        triarea= height*base/2

        # Inserting the results to the display box
        displayBox.config(state="normal")#  makes box editable
        displayBox.insert(END, "Triangle Area: " + str(triarea) + "u Sq\n\n")
        displayBox.config(state="disable")#  makes box uneditable

    # Calculates the circle area
    if calccirc:

        # putting entry into float variable
        radius = float(radiusentry.get())

        # math to calculate the area of the circle
        circarea= radius**2*math.pi

        # outputting result to the display box
        displayBox.config(state="normal")  # making the display box editable
        displayBox.insert(END, "Circle Area: "+str(circarea)+"u Sq\n\n")
        displayBox.config(state="disable")  # making the display box non editable



# ***********************************************************************************************************************

# Declaring the labels and entries
lengthlabel =Label(page1, text="Length", bg=backgroundcolour)
lengthentry = Entry(page1)
radiuslabel = Label(page1, text="Radius", bg=backgroundcolour)
radiusentry = Entry(page1)
heightlabel = Label(page1, text="Height", bg=backgroundcolour)
heightentry = Entry(page1)
widthlabel = Label(page1, text="Width", bg=backgroundcolour)
widthentry = Entry(page1)
baselabel = Label(page1, text="Base", bg=backgroundcolour)
baseentry = Entry(page1)

# buttons(Rect,Tri,Circle,Run)
# these buttons create entries and labels also gets rid of other labels and entries
Rectangle = Button(page1, text="Rectangle", command=rect, bg=buttonbgcolour, fg=buttonfgcolour)
Rectangle.place(x=10, y=5, width=80)

Triangle = Button(page1, text="Triangle", command=tri, bg=buttonbgcolour, fg=buttonfgcolour)
Triangle.place(x=100, y=5, width=80)

Circle = Button(page1, text="Circle", command=circ, bg=buttonbgcolour, fg=buttonfgcolour)
Circle.place(x=190, y=5, width=80)

# this button runs the calculations by calling the run function
Run = Button(page1, text="Run", bg="green", fg="white", command=run)
Run.place(x=113, y=35, width=50)

# Creating the text box
displayBox=Text(page1)
displayBox.pack(padx=10,pady=(160,15))
displayBox.insert(END,"Result: \n\n")
displayBox.config(state="disable", bg=bgcolour, fg=fgcolour)  # Setting the colour as well as making it non-editable

# </editor-fold>

# <editor-fold desc="Page 2 Code">
# PAGE 2 Random

# Creating labels and entries
lowerlabel =Label(page2, text="Lower limit", bg=backgroundcolour)
lowerentry = Entry(page2)
upperlabel = Label(page2, text="Upper limit", bg=backgroundcolour)
upperentry = Entry(page2)
numofrandl = Label(page2, text="#of Random #s", bg=backgroundcolour)
numofrande = Entry(page2)
sortB = Button(page2,text="Sort",command=sortran,bg=buttonbgcolour,fg=buttonfgcolour)

# Packing the labels and entries
lowerlabel.pack()
lowerentry.pack()
upperlabel.pack(pady=(5,0))
upperentry.pack()
numofrande.place(x=220,y=59,width=30)
numofrandl.place(x=190,y=43)
sortB.place(x=20,y=20)


# Function ranrun(RandomRun) this calculates a number between the set parameters
def ranrun(*args):

    # Putting the entries into variables
    lower = int_or_float(lowerentry.get())
    upper = int_or_float(upperentry.get())

    # telling the person off if they try to put the lower limit higher than the upper limit
    if lower>upper:
        displayran.config(state="normal")
        displayran.insert(END,"Who do you think you are putting the lower bigger then upper!\n\n")
        displayran.config(state="disable")

    # checking if they gave me a float. if they did I tell them not to.
    if isinstance(lower,float) or isinstance(upper,float):
        displayran.config(state="normal")
        displayran.insert(END, "HEY are you trying to give me decimals don't do that!\n\n")
        displayran.config(state="disable")

    # Making sure it does not work with decimals because it is weird
    if isinstance(lower,int) and isinstance(upper,int):
        global rangeofran, ranlist
        ranlist=[]

        # checks how many random numbers to make if no value is there it makes it = 1
        try:
            rangeofran = int(numofrande.get())
        except:
            rangeofran = 1

        # displaying the random list of numbers
        for i in range(int(rangeofran)):
            ranlist.append(random.randint(int(lower), int(upper)))
            displayran.config(state="normal")
            displayran.insert(END, "Random Number: "+str(ranlist[i])+"\n\n")
            displayran.config(state="disable")
            rangeofran = len(ranlist)

# Creating the display box
displayran = ScrolledText(page2)
displayran.config(state="normal")
displayran.insert(END, "Random Number Generator\n\n")
displayran.config(state="disable")

# Creating the button that calls ranrun
randomButton=Button(page2,text="Run", command=ranrun, bg=buttonbgcolour, fg=buttonfgcolour)
randomButton.pack(pady=(5,0))
displayran.pack(pady=10,padx=10)

# </editor-fold>

# <editor-fold desc="Page 3 Code">
# PAGE 3

# <editor-fold desc="Creating the Canvas">

# Creating a new canvas on page3 named draw
draw=Canvas(page3)

# Giving the canvas a white background
draw.config(bg="white")

# Making the canvas the desired height and width
draw.place(x=0,y=90,width=285, height=500)

# </editor-fold>

# <editor-fold desc = "Creating Variables">

# Declaring Booleans
drawCircB=False
drawRectB=False
drawTriB=False

# This is where the top left of the shape is drawn
startx=50
starty=30

# Makes the labels and entries for inputting info

# Rectangle
rectLenLabel = Label(page3, text="Length", bg=backgroundcolour)
rectWidLabel = Label(page3, text="Width", bg=backgroundcolour)
rectWidEntry = Entry(page3)
rectLenEntry = Entry(page3)

# Triangle
triHighLabel = Label(page3, text="Height", bg=backgroundcolour)
triBaseLabel = Label(page3, text="Base", bg=backgroundcolour)
triHighEntry = Entry(page3)
triBaseEntry = Entry(page3)

# Ellipse
ellipseRadiusXLabel = Label(page3, text="RadiusX", bg=backgroundcolour)
ellipseRadiusXEntry = Entry(page3)
ellipseRadiusYLabel = Label(page3, text="RadiusY", bg=backgroundcolour)
ellipseRadiusYEntry = Entry(page3)


# </editor-fold>


# Creates the entry boxes and labels for rectangle
def drawRect(*args):

    # Disables the buttons pressed and reinstates the others
    drawR.config(state="disable")
    drawT.config(state="normal")
    drawE.config(state="normal")

    # Places the labels and entries needed for the rectangle
    rectLenLabel.place(x=19, y=40, width=70)
    rectLenEntry.place(x=19, y=65, width=70)
    rectWidLabel.place(x=180, y=40, width=70)
    rectWidEntry.place(x=180, y=65, width=70)

    # Forgets all other labels and entries to make room
    # (Triangle)
    triBaseLabel.place_forget()
    triBaseEntry.place_forget()
    triHighLabel.place_forget()
    triHighEntry.place_forget()

    # (Ellipse)
    ellipseRadiusXEntry.place_forget()
    ellipseRadiusXLabel.place_forget()
    ellipseRadiusYEntry.place_forget()
    ellipseRadiusYLabel.place_forget()

    # Tells the drawRun what to calculate (Rectangle)
    global drawCircB,drawTriB,drawRectB
    drawCircB = False
    drawRectB = True
    drawTriB = False


# Creates the entry boxes and labels for triangle
def drawTri(*args):

    # Disables the button pressed and reinstates the others
    drawR.config(state="normal")
    drawT.config(state="disabled")
    drawE.config(state="normal")

    # Places the labels and entries needed for the triangle
    triBaseLabel.place(x=19, y=40, width=70)
    triBaseEntry.place(x=19, y=65, width=70)
    triHighLabel.place(x=180, y=40, width=70)
    triHighEntry.place(x=180, y=65, width=70)

    # Forgets all other labels and entries to make room
    rectLenLabel.place_forget()
    rectLenEntry.place_forget()
    rectWidLabel.place_forget()
    rectWidEntry.place_forget()

    ellipseRadiusXEntry.place_forget()
    ellipseRadiusXLabel.place_forget()
    ellipseRadiusYEntry.place_forget()
    ellipseRadiusYLabel.place_forget()

    # Tells the drawRun what to calculate (Triangle)
    global drawCircB, drawTriB, drawRectB
    drawCircB = False
    drawRectB = False
    drawTriB = True


# Creates the entry boxes and labels for ellipse
def drawEllipse(*args):

    # Disables the button pressed and reinstates the others
    drawR.config(state="normal")
    drawT.config(state="normal")
    drawE.config(state="disable")

    # Places the needed labels and entries for the ellipse
    ellipseRadiusXLabel.place(x=19, y=40, width=70)
    ellipseRadiusXEntry.place(x=19, y=65, width=70)
    ellipseRadiusYLabel.place(x=180, y=40, width=70)
    ellipseRadiusYEntry.place(x=180, y=65, width=70)

    # Forgets the other labels and entries to make room
    rectLenLabel.place_forget()
    rectLenEntry.place_forget()
    rectWidLabel.place_forget()
    rectWidEntry.place_forget()

    triBaseLabel.place_forget()
    triBaseEntry.place_forget()
    triHighLabel.place_forget()
    triHighEntry.place_forget()

    # Tells drawRun what to calculate (Ellipse)
    global drawCircB, drawTriB, drawRectB
    drawCircB = True
    drawRectB = False
    drawTriB = False


# Does the calculations and displays for the shape wanted
def drawRun(*args):

    # This deletes the previous shapes
    draw.addtag_all("shape")
    draw.delete("shape")

    if drawRectB:

        # Creating variables from the entries
        rectDrawLen=int(rectLenEntry.get())
        rectDrawWidth=int(rectWidEntry.get())
        x=rectDrawWidth
        y=rectDrawLen

        # Scaling the shape to the size of the screen
        # Smaller
        while x>185:
            x=x*0.999
            y=y*0.999

        while y>330:
            x = x * 0.999
            y = y * 0.999

        # Bigger
        while x < 165 and y < 320:
            x = x * 1.001
            y = y * 1.001

        while x < 165 and y < 320:
            x = x * 1.001
            y = y * 1.001

        # Labels the sides
        draw.create_text(15,y/2+30,text=rectDrawLen)
        draw.create_text(x/2+50, 10,text=rectDrawWidth)
        x += startx
        y += starty

        # Draws the rectangle
        draw.create_rectangle(startx, starty, x, y)

    if drawTriB:

        # Creates variables with the entries
        triBase=triBaseEntry.get()
        triHigh=triHighEntry.get()
        x=int(triBase)
        y=int(triHigh)

        # Scaling
        # Smaller
        while x>185:
            x=x*0.9999
            y=y*0.9999
            print("x:",x)
            print("y:",y)
        while y>330:
            x = x * 0.9999
            y = y * 0.9999
            print("x:", x)
            print("y:", y)

        # Bigger
        while x < 165 and y < 320:
            x = x * 1.001
            y = y * 1.001
            print("x:", x)
            print("y:", y)
        while x < 165 and y < 320:
            x = x * 1.001
            y = y * 1.001
            print("x:", x)
            print("y:", y)

            # Draws the triangle
        draw.create_polygon(startx,y+starty,x/2+startx,starty,x+startx,y+starty)

    if drawCircB:

        # Creates variables with the entries
        x = int(ellipseRadiusXEntry.get())
        y = int(ellipseRadiusYEntry.get())
        xd = x*2
        yd = y*2

        # Scaling
        # Smaller
        while xd>185:
            xd=xd*0.9999
            yd=yd*0.9999
            print("x:",xd)
            print("y:",yd)
        while yd>330:
            xd = xd * 0.9999
            yd = yd * 0.9999
            print("x:", xd)
            print("y:", yd)

        # Bigger
        while xd < 165 and yd < 320:
            xd = xd * 1.001
            yd = yd * 1.001
            print("x:", xd)
            print("y:", yd)
        while xd < 165 and yd < 320:
            xd = xd * 1.001
            yd = yd * 1.001
            print("x:", xd)
            print("y:", yd)

        # Drawing radius lines
        draw.create_line(startx+xd/2,starty+yd/2,startx+xd,starty+yd/2,dash=3)
        draw.create_line(startx+xd/2,starty+yd/2,startx+xd/2,starty,dash=3)

        # Drawing the ellipse
        draw.create_oval(startx,starty,xd+startx,yd+starty)

        # Labeling the radius lines
        draw.create_text(xd/2-20+startx, yd/4+starty, text=str(y))
        draw.create_text(xd*(3/4) + startx, yd/2+15+starty, text=str(x))


# <editor-fold desc="Buttons">

# Creating the buttons
drawR = Button(page3,text="Rectangle", command=drawRect, bg=buttonbgcolour, fg=buttonfgcolour)
drawR.place(x=20, y=10, width=70)

drawT = Button(page3,text="Triangle", command=drawTri, bg=buttonbgcolour, fg=buttonfgcolour)
drawT.place(x=100, y=10, width=70)

drawE = Button(page3, text="Ellipse", command=drawEllipse, bg=buttonbgcolour, fg=buttonfgcolour)
drawE.place(x=180, y=10, width=70)

runDraw = Button(page3,text="Run", command=drawRun, bg="green", fg="white")
runDraw.place(x=120, y=50, )

# </editor-fold>

# </editor-fold>

# <editor-fold desc="Page 4 Code">

# Declaring Variables
color = ""

y=int
x=int

oldy=int
oldx=int

# Makes the colour = red (called by button)
def red():
    global color
    color = "red"

# Makes the colour = blue (called by button)
def blue():
    global color
    color = "blue"


# Makes the colour = yellow (called by button)
def yellow():
    global color
    color = "yellow"


# Makes the colour = orange (called by button)
def orange():
    global color
    color = "orange"


# Makes the colour = purple (called by button)
def purple():
    global color
    color = "purple"


# Makes the colour = pink (called by button)
def pink():
    global color
    color = "pink"


# Makes the colour = green (called by button)
def green():
    global color
    color = "green"


# Makes the colour = white (called by button)
def white():
    global color
    color = "white"


# Clears the screen of drawings  (called by button)
def clear():
    drawingC.addtag_all("drawing")
    drawingC.delete("drawing")

# Sets the colour as what was put in the custom colour box (called by button)
def setCustom():
    global color
    color = custom.get()
    custom.delete(0,END)

# Creates a canvas
drawingC= Canvas(page4)

# Configures the background to be white
drawingC.config(bg="white")

# Configures the size, packs and places the canvas
drawingC.place(x=0,y=50,width=285, height=500)


# this function draws and is called by a bind (B1-Motion)
def callback(event):
    global size, x, y,oldx,oldy

    # makes the size = to what is in the size box
    try:
        size = int(sizeEntry.get())
    # if no size is in the box it sets the size to one
    except ValueError:
        size = 1

    # sets a cap of the size at 4
    if size>4:
        size = 4

    # puts the current location in the x and y variables
    x = event.x
    y = event.y


    # if they are 0 it means it has been lifted up therfore it should not draw from (0,0)
    if oldx is not 0 and oldy is not 0 and y is not 0 and x is not 0:
        drawingC.create_line(oldx, oldy, x, y, fil=color,smooth=TRUE,width=size*2)

        # makes the size work
        for i in range(size):

            drawingC.create_line(oldx + i, oldy - size, x + i, y+size, fill=color, )
            drawingC.create_line(oldx - i, oldy - size, x - i, y+size, fil=color, )
            drawingC.create_line(oldx + i, oldy + size, x + i, y + size, fill=color, )
            drawingC.create_line(oldx - i, oldy - size, x - i, y - size, fil=color, )

    # puts the current x and y as old x and y to be used next time
    oldx = event.x
    oldy = event.y

def b1up(*args):
    global oldx,oldy
    oldy,oldx,x,y=0,0,0,0
b1up()

# makes it so the default colour is red
red()


# Creates all of the buttons
clearB=Button(page4, text="Clear", command = clear)
clearB.place( x=40,y=40)\

sizeLabel = Label(page4, text="Size", bg=backgroundcolour)
sizeLabel.place(x=250,y=1)

sizeEntry = Entry(page4)
sizeEntry.place(x=250,y=20,width=25)

red = Button(page4, bg="red", command = red)
red.place(x=5,y=5)

blue = Button(page4, bg="blue", command = blue)
blue.place(x=20,y=5)

yellow = Button(page4, bg="yellow", command = yellow)
yellow.place(x=35,y=5)

orange = Button(page4, bg="orange", command = orange)
orange.place(x=50,y=5)

purple = Button(page4, bg="purple", command = purple)
purple.place(x=65,y=5)

pink = Button(page4, bg="pink", command = pink)
pink.place(x=80,y=5)

white = Button(page4, bg="white", command = white)
white.place(x=95,y=5)

custom = Entry(page4)
custom.place(x=110,y=25,width=60)
customset = Button(page4,text="Set",command=setCustom)
customset.place(x=180,y=25,height = 22)
customl = Label(page4,text="Custom Colour(Hex#)",bg="grey")
customl.place(x=110,y=5)


# binds the mouse buttons
drawingC.bind("<B1-Motion>",callback)
drawingC.bind("<ButtonRelease-1>", b1up)

#</editor-fold>

# <editor-fold desc="Page 5 Code">


# This when called creates the game canvas (gameC) and creates the grass aesthetic. It also makes new bird and pipe
# Objects based off the classes. Then it calls drawG
def init():
    # Makes the Game Canvas available to the classes and bird and pipe available to drawG Function.
    global gameC, bird, pipe,quitf
    quitf = False
    root.unbind_all(root)
    gameC = Canvas(page5, width=300, height=500)
    gameC.place(x=0, y=0)
    gameC.config(bg="lightblue")
    grass = gameC.create_rectangle(0, 500, 300, 400, fill="green")

    bird = Bird()
    pipe = Pipes()


    drawG()


# As long as the person has not gone to the leaderboards it calls update bird and update pipe (every 17 milliseconds)
def drawG():

    if quitf==False:
        bird.update()
        pipe.update()

        root.after(17, drawG)


# this class creates the bird including its drawing
class Bird:

    def __init__(self):
        global gameC

        # Declaring variables
        self.height = 390
        self.y = 150
        self.x = 40

        self.lift = -5.5
        self.gravity = 0.2
        self.velocity = -7
        self.timer = 0

        # Creates the bird on the canvas
        self.bird = gameC.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="red")

        # Binds W to function "fly"
        root.bind("<w>",self.fly)

    # called every 17 millisecond and updates all of the birds attributes
    def update(self):

        # creates the gravity effect
        self.velocity += self.gravity

        # moves the bird according to velocity
        self.y += self.velocity

        # Calls function "show"
        self.show()

        # Makes the bird bounce when hitting the ground
        if self.y > self.height:
            self.y = self.height
            self.velocity= -self.velocity/2

        # Makes it so the bird cannot go above the screen
        if self.y < 0:
            self.y = 0
            self.velocity= 0

    # Updates the bird location
    def show(self):
        gameC.coords(self.bird,self.x, self.y, self.x+20,self.y+20)

    # sets the velocity of the bird when "w" is pressed
    def fly(self,*args):
        self.velocity=self.lift


# this class creates the pipes and deals with collision and game over
class Pipes:
    def __init__(self):

        # Declares variables
        self.gap = 150
        self.moveSpeed = -3
        self.x = 350
        self.y = random.randint(10,250)
        self.score = 0
        self.lost = False

        # Creates the top and bottom of the pipe
        self.pipe = gameC.create_rectangle(self.x,0,self.x+20,self.y, fill="lightgreen")
        self.pipeu = gameC.create_rectangle(self.x,400,self.x+20,self.y +self.gap, fill="lightgreen")

        # Creates the score label
        self.scorel = Label(page5,text = "Score: ", bg="lightblue")
        self.scorel.place(x=220,y=20)

    # calls functions "move" and "collision" and updates the score and speeds up the movement
    # (every 17 milliseconds)
    def update(self):
        self.move()
        self.collision()

        # Updates the score
        self.scorel.config(text="Score: " + str(self.score))

        # Checks if the player has not lost
        if self.lost==False:
            # Speeds up the game slowly
            if self.moveSpeed > -4.5:
                self.moveSpeed-=0.001

    # moves the x according to speed, moves the drawing, and repositions the pipe
    def move(self):
        # updates the x locations
        self.x += self.moveSpeed

        # redraws the new position
        gameC.coords(self.pipe, self.x, 0, self.x + 20, self.y)
        gameC.coords(self.pipeu, self.x, 400, self.x + 20, self.y+self.gap)

        # if the pipe goes off the screen put it back to the front
        if self.x<-15:
            self.x=310
            # different gap location
            self.y = random.randint(10,240)
            # +1 score
            self.score += 1

            # check the size of the gap
            if self.gap > 90:
                # if the gap is not smaller than 90 make the gap smaller
                # making it harder for the player
                self.gap-=1.2
        # if the player has lost slow down the movement.
        if self.lost:
            self.moveSpeed= self.moveSpeed*0.982

    # Checks for collision
    def collision(self):

        # Checks the x and y to see if they are the same
        if bird.x+20 > self.x and bird.y < self.y and bird.x<self.x+20 or bird.y+20 > self.y+self.gap and bird.x +20 > self.x and bird.x < self.x+20:

            # Checks to see if the bird is in the pipe at the time of the collision
            # if it is that means it hit the top of bottom meaning instead of bouncing
            # back it should keep going with a -velocity so it looks like it bounced
            if bird.x+17 >self.x:
                bird.velocity = -bird.velocity/1.4
            # if it was not in between the pipes when the collision occurred then it should bounce back
            else:
                self.moveSpeed = -self.moveSpeed

            # unbinds "w" so you can no longer fly
            root.unbind("<w>")

            # changes self.lost to True so operations stop
            self.lost = True

            # Places a button to bring you to the high scores page
            self.retryFlapB=Button(page5,text="HighScores", command = self.retryFlap)
            self.retryFlapB.place(x=100,y=100,width=90)

    # called when player presses the highscores button
    def retryFlap(self):
        global quitf
        # Lifts the play button so the player can play again
        play.lift()

        # Calls leaderBoards bringing up the high score
        self.leaderBoards()

        # tells the game the player has closed the game
        quitf=True

        # Destroys the game canvas
        gameC.destroy()

    # checks to see if you have the new highscore and places your score in a list if it is in the top 5
    def leaderBoards(self):

        lblist = []

        # opens a file
        try:
            lb = open("lb.txt", "r+")
        except FileNotFoundError:
            # Creates a new file if one does not already exists
            lb = open("lb.txt","w")
            lb.write("0\n")
            lb.write("0\n")
            lb.write("0\n")
            lb.write("0\n")
            lb.write("0")
            # Closes the file and opens it to read
            lb.close()
            lb = open("lb.txt","r")

        # Reads lines separately adding them to a list
        lbl = lb.readlines()
        for i in lbl:
            lblist.append(int(i))
        # closes the file
        lb.close()
        # opens a file to write
        lb = open("lb.txt","w")
        # Adds your score to the list
        lblist.append(self.score)

        # Sorts the list lowest to highest
        selectionSort(lblist)
        # Flips the list so it is highest to lowest
        lblist.reverse()

        # Takes the top 5 and puts them in the file
        for i in range(5):
            lb.write(str(lblist[i])+"\n")

        # Displays the top score
        self.hi1 = Label(page5, text=str(lblist[0]))
        self.hil = Label(page5, text="HighScore",bg="red",fg="white")
        self.hi1.place_forget()
        self.hil.place_forget()
        self.hil.place(x=100,y=150,width=90)
        self.hi1.place(x=100,y=170,width=90)

# this function is called by a button it initializes the game
def playButton():
    init()

# Creates the play button
play = Button(page5,text= "Play Flappy",bg="green",fg="white", command = playButton)
play.place(x= 100, y= 100,width = 90)

# ****************************************************************************
# END OF FLAPPY BIRD PAGE 5 CODE**********************************************
# ****************************************************************************
#</editor-fold>

# <editor-fold desc="Page 6 Code">


# Initializes Snake
def snakeInit():
    global snakeC,snake,scale,sss,food,total,quitsnake
    # declaring variables
    quitsnake = False
    sss = 10
    scale = 10

    # Creating the snake canvas
    snakeC = Canvas(page6,width=285,height=500)
    snakeC.place(x=0,y=0)

    # Creating objects based off the classes
    snake = Snake()
    food = Food()

    # calling draw snake
    drawsnake()


# Called every 150 milliseconds
def drawsnake():

    # making sure the player has not quit yet
    if not quitsnake:
        # Updates the snake
        snake.update()
        snake.show()

        # calls itself after 150 milliseconds
        root.after(150,drawsnake)


# Creates the snake
class Snake():
    # declares the variables binds the keys and creates the first body piece
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speed=1
        self.xspeed = 0
        self.yspeed = 0
        self.total = 0
        self.score = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.scorel = Label(page6, text="Score: 0",bg="white")
        self.scorel.place(x=210, y=20)
        self.back = snakeC.create_rectangle(10,10,270,470,fill="white")
        self.tailx = []
        self.taily = []
        root.bind("<a>",self.leftb)
        root.bind("<d>", self.rightb)
        root.bind("<w>", self.upb)
        root.bind("<s>", self.downb)
        root.bind("<q>", self.grow)
        self.tail = []
        self.tail.append(snakeC.create_rectangle(self.x, self.y, self.x + 10, self.y + 10,fill="green"))

    # updates the x and y
    def update(self):


        self.x += self.xspeed
        self.y += self.yspeed
        self.eat()
        self.collision()

    # moves the snake
    def show(self):
        # puts the first piece at the back
        self.tail.append(self.tail[0])
        # deletes the one at the front because it is at the back now
        del self.tail[0]
        # and moves the new front piece
        snakeC.coords(self.tail[0], self.x, self.y, self.x + scale, self.y + scale)

    # Binding functions that move change the x and y speed
    # (Left)
    def leftb(self,*args):
        if not self.right:
            self.xspeed = -self.speed*scale
            self.yspeed = 0
            self.left = True
            self.right = False
            self.up = False
            self.down = False

    # (Right)
    def rightb(self,*args):
        if not self.left:
            self.xspeed = self.speed*scale
            self.yspeed = 0
            self.left = False
            self.right = True
            self.up = False
            self.down = False

    # (Up)
    def upb(self,*args):
        if not self.down:
            self.yspeed = -self.speed*scale
            self.xspeed = 0
            self.left = False
            self.right = False
            self.up = True
            self.down = False

    # (Down)
    def downb(self,*args):
        if not self.up:
            self.yspeed = self.speed*scale
            self.xspeed = 0
            self.left = False
            self.right = False
            self.up = False
            self.down = True

    # Checks for collision
    def collision(self):
        # checking collision with walls
        if self.y > 470-scale:
            self.die()
        if self.y<scale:
            self.die()
        if self.x > 270-scale:
            self.die()
        if self.x<scale:
            self.die()

        # Checking collision with self
        for i in range(len(self.tail)-2,):
            if snakeC.coords(self.tail[-1]) == snakeC.coords(self.tail[i]):
                self.die()

    # this function handles the food
    def eat(self,*args):
        # Checking collision with food
        if self.x == food.x and self.y == food.y:
            # Give a new location for the food
            food.x = random.randint(2, 25) * scale
            food.y = random.randint(2, 44) * scale
            snakeC.coords(food.food, food.x, food.y, food.x + scale, food.y + scale)
            # add 3 tail sections
            self.total+=3
            self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                     random.randint(5000, 100000), random.randint(5000, 100000),
                                                     fill="green"))
            self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                     random.randint(5000, 100000), random.randint(5000, 100000),
                                                     fill="green"))
            self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                     random.randint(5000, 100000), random.randint(5000, 100000),
                                                     fill="green"))

            # Adding 1 score
            self.score +=1

            # Updating the score label
            self.scorel.config(text = "Score: "+str(self.score))

    # This is a cheat code to grow (Press "Q")
    def grow(self,*args):
        self.total += 3
        self.score += 1
        self.scorel.config(text="Score: " + str(self.score))
        self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                 random.randint(5000, 100000), random.randint(5000, 100000),
                                                 fill="green"))
        self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                 random.randint(5000, 100000), random.randint(5000, 100000),
                                                 fill="green"))
        self.tail.append(snakeC.create_rectangle(random.randint(5000, 100000), random.randint(5000, 100000),
                                                 random.randint(5000, 100000), random.randint(5000, 100000),
                                                 fill="green"))

    # this is called to when you collide
    def die(self):
        global scale,quitsnake
        quitsnake = True

        # makes a button to bring you to highscore page
        self.retryFlapB = Button(page6, text="HighScore", command=self.highscorepage)
        self.retryFlapB.place(x=100, y=100, width=90)

        # sets the speed to 0 so the snake does not move
        self.speed = 0
        self.xspeed = 0
        self.yspeed = 0

        # unbinds the buttons so you cannot make the snake move
        root.unbind_all(root)

    # called when you click the
    def highscorepage(self):
        global quitf

        # changes the background of the score to make it blend in
        self.scorel.config(bg="grey")

        # lifts the play button so the player may play again
        playsnake.lift()

        # Destroys the snake game canvas
        snakeC.place_forget()
        snakeC.destroy()

        # opens a high score file
        try:
            lbs = open("lbs.txt", "r+")
        except FileNotFoundError:
            # Creates a new file if one does not already exists
            lbs = open("lbs.txt","w")
            lbs.write("0")
            lbs.close()
            lbs = open("lbs.txt","r+")

        # checks if your score is higher than the one in the file
        if self.score>int(lbs.read()):
            # if it is it deletes the score in the file
            lbs.seek(0)
            lbs.truncate()
            # and replaces it with your score
            lbs.write(str(self.score))
        # closes the file
        lbs.close()
        # opens the file this time to read not write
        lbs = open("lbs.txt","r")
        self.high = lbs.read()
        # display the high score in a label
        self.hi1 = Label(page6, text=self.high)
        self.hil = Label(page6, text="HighScore", bg="red", fg="white")
        self.hi1.place_forget()
        self.hil.place_forget()
        self.hil.place(x=100, y=150, width=90)
        self.hi1.place(x=100, y=170, width=90)

# food is a red square with an x and y
class Food():
    def __init__(self):

        self.scale=10
        self.x = random.randint(1,25)*self.scale
        self.y = random.randint(1,46)*self.scale
        self.food = snakeC.create_rectangle(self.x, self.y, self.x + self.scale, self.y + self.scale, fill="red")

# play button is called by button and initializes the snake game
def playButton():

    snakeInit()

# creates the play button
playsnake = Button(page6,text= "Play Snake",bg="green",fg="white", command = playButton)
playsnake.place(x= 100, y= 100,width = 90)

#"""
#</editor-fold>

root.mainloop()