from tkinter import *

root = Tk()

one = Label(root, text = "One",fg = "black" ,bg = "white")
one.pack()
two = Label(root, text = "Two",fg = "black" ,bg = "white")
two.pack(fill = X)
three = Label(root, text = "Three",fg = "black" ,bg = "white")
three.pack(side = RIGHT,fill = Y) #fills to Y axis according to window

root.mainloop()
