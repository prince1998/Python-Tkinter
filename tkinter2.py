from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "red")
button2 = Button(topFrame, text = "Button 2", fg = "blue")#fg - text 
button3 = Button(topFrame, text = "Button 3", fg = "black")
button4 = Button(bottomFrame, text = "Button 4", fg = "green")

button1.pack(side = RIGHT) #pack this button and place it as left as possible in top frame
button2.pack(side = TOP)
button3.pack(side = LEFT)
button4.pack(side = LEFT)


root.mainloop()