from tkinter import *

root = Tk()

def first(event):
	print("Hello, I pressed Left")
	
def second(event):
	print("Hello, My pressed right")
	
frame = Frame(root,width = 300,height = 250)
frame.bind("<Button-1>", first)

frame.bind("<Button-2>", second)
frame.pack()


root.mainloop()