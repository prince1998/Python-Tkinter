from tkinter import *

def doNothing():
	print("I wont do anything :P")
	
root = Tk()

#*************** MAIN MENU ***************

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

#***********Toolbar*****************

toolbar = Frame(root, bg= "red") #created basic toolbar
 
insertButton = Button(toolbar,text="Insert Image",command = doNothing) #added buttons in toolbar
insertButton.pack(side = LEFT, padx = 2,pady = 2 )#for displaying, padding : extra space
 
printButton = Button(toolbar, text = "Print", command = doNothing)
printButton.pack(side = LEFT, padx = 2,pady = 2)
 
toolbar.pack(side = TOP, fill = X) #placed under menu
 
#Status Bar

status = Label(root,text = "Download Sona",bd = 1, relief = SUNKEN, anchor = W) #bd : Border, anchor - align text west, 
status.pack(side = BOTTOM, fill = X)





root.mainloop()