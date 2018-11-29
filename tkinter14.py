from tkinter import *

root = Tk()

photo = PhotoImage(file="screen.png")

label = Label(root,image=photo)

label.pack()

root.mainloop()