from tkinter import *

def doNothing():
	print("I wont do anything :P")
	
root = Tk()
frame = Frame(root)
frame.pack()
menu = Menu(root) #Creates a menu
root.config(menu=menu)

subMenu = Menu(menu)

menu.add_cascade(label = "File",menu = subMenu)#Adds menu item
subMenu.add_command(label = "Open",command = doNothing)#Adds drop down items and its functionality
subMenu.add_command(label = "Save",command = doNothing)

subMenu.add_separator()

subMenu.add_command(label= "Exit", command = frame.quit)
subMenu1 = Menu(menu)
menu.add_cascade(label = "Edit",menu = subMenu1)
subMenu1.add_command(label= "Undo",command = doNothing)
subMenu1.add_command(label = "Redo",command = doNothing)
subMenu1.add_separator()

subMenu1.add_command(label = "Exit",command = frame.quit)

root.mainloop()