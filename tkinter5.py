from tkinter import *

root = Tk()

def printName():
	print("Hello, my name is Priyansh")
	
button_1 = Button(root,text = "Print my name", command = printName)
button_1.pack()

root.mainloop()