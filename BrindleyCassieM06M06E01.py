from tkinter import *

def toFahrenheit():
    res = (9/5) * float(e1.get()) + 32
    myText.set(res)

root = Tk()
myText = StringVar();

firstFrame = Frame(root)
firstFrame.pack

secondFrame = Frame(root)
secondFrame.pack (side = BOTTOM)

Label (firstFrame, text= 'Celsius').grid(row = 0)

Label (firstFrame, text= 'Fahrenheit').grid(row = 1)

Label (firstFrame, text= 'Result').grid(row = 2)

e1 = Entry(firstFrame)
e2 = Entry(firstFrame)

e1.grid(row = 0, column = 1)